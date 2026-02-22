from sqlmodel import SQLModel

class EmpleadoCreate(SQLModel):
    nombre: str
    email: str
    salario: float
    departamento_id: int

class EmpleadoUpdate(SQLModel):
    nombre: str | None = None
    email: str | None = None
    salario: float | None = None
    departamento_id: int | None = None

class EmpleadoResponse(SQLModel):
    id: int
    nombre: str
    email: str
    salario: float
    departamento_id: int
