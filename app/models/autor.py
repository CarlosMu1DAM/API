from sqlmodel import SQLModel, Field
from typing import Optional

class Empleado(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    salario: float
    departamento_id: int = Field(foreign_key="departamento.id")
