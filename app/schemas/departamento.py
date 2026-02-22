from sqlmodel import SQLModel

class DepartamentoCreate(SQLModel):
    nombre: str

class DepartamentoUpdate(SQLModel):
    nombre: str | None = None

class DepartamentoResponse(SQLModel):
    id: int
    nombre: str
