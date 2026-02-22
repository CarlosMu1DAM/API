from fastapi import FastAPI
from app.db.session import create_db_and_tables
from app.routers import empleados, departamentos

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(empleados.router)
app.include_router(departamentos.router)

