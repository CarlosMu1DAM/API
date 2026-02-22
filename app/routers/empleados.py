from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.empleado import EmpleadoCreate, EmpleadoUpdate, EmpleadoResponse
from app.services.empleado_service import EmpleadoService

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.post("/", response_model=EmpleadoResponse, status_code=status.HTTP_201_CREATED)
def create_empleado(data: EmpleadoCreate, session: Session = Depends(get_session)):
    return EmpleadoService(session).create(data)

@router.get("/", response_model=list[EmpleadoResponse])
def get_empleados(session: Session = Depends(get_session)):
    return EmpleadoService(session).get_all()

@router.get("/{id}", response_model=EmpleadoResponse)
def get_empleado(id: int, session: Session = Depends(get_session)):
    return EmpleadoService(session).get_by_id(id)

@router.put("/{id}", response_model=EmpleadoResponse)
def update_empleado(id: int, data: EmpleadoUpdate, session: Session = Depends(get_session)):
    return EmpleadoService(session).update(id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_empleado(id: int, session: Session = Depends(get_session)):
    EmpleadoService(session).delete(id)
