from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.db.session import get_session
from app.services.departamento_service import DepartamentoService
from app.schemas.departamento import (
    DepartamentoCreate,
    DepartamentoResponse,
    DepartamentoUpdate,
)

router = APIRouter(prefix="/departamentos", tags=["Departamentos"])


@router.post("/", response_model=DepartamentoResponse, status_code=status.HTTP_201_CREATED)
def create_departamento(
        departamento: DepartamentoCreate,
        session: Session = Depends(get_session),
):
    return DepartamentoService(session).create(departamento)


@router.get("/", response_model=list[DepartamentoResponse])
def read_departamentos(session: Session = Depends(get_session)):
    return DepartamentoService(session).get_all()


@router.get("/{id}", response_model=DepartamentoResponse)
def read_departamento(id: int, session: Session = Depends(get_session)):
    return DepartamentoService(session).get_by_id(id)


@router.patch("/{id}", response_model=DepartamentoResponse)
def update_departamento(
        id: int,
        departamento_data: DepartamentoUpdate,
        session: Session = Depends(get_session),
):
    return DepartamentoService(session).update(id, departamento_data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_departamento(id: int, session: Session = Depends(get_session)):
    DepartamentoService(session).delete(id)
