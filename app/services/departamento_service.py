from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.departamento import Departamento
from app.schemas.departamento import (DepartamentoCreate, DepartamentoUpdate, DepartamentoResponse,)


class DepartamentoService:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: DepartamentoCreate) -> Departamento:
        departamento = Departamento.model_validate(data)
        self.session.add(departamento)
        self.session.commit()
        self.session.refresh(departamento)
        return departamento

    def get_all(self):
        return self.session.exec(select(Departamento)).all()

    def get_by_id(self, id: int):
        departamento = self.session.get(Departamento, id)
        if not departamento:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return departamento

    def update(self, id: int, data: DepartamentoUpdate):
        departamento = self.get_by_id(id)

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(departamento, key, value)

        self.session.add(departamento)
        self.session.commit()
        self.session.refresh(departamento)
        return departamento

    def delete(self, id: int):
        departamento = self.get_by_id(id)
        self.session.delete(departamento)
        self.session.commit()
