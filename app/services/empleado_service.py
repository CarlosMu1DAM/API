from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.autor import Empleado
from app.schemas.empleado import EmpleadoCreate, EmpleadoUpdate

class EmpleadoService:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.exec(select(Empleado)).all()

    def get_by_id(self, empleado_id: int):
        empleado = self.session.get(Empleado, empleado_id)
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return empleado

    def create(self, data: EmpleadoCreate):
        empleado = Empleado.model_validate(data)
        self.session.add(empleado)
        self.session.commit()
        self.session.refresh(empleado)
        return empleado

    def update(self, empleado_id: int, data: EmpleadoUpdate):
        empleado = self.get_by_id(empleado_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(empleado, key, value)
        self.session.add(empleado)
        self.session.commit()
        self.session.refresh(empleado)
        return empleado

    def delete(self, empleado_id: int):
        empleado = self.get_by_id(empleado_id)
        self.session.delete(empleado)
        self.session.commit()
