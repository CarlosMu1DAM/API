Descripción:
API REST desarrollada con FastAPI que permite gestionar empleados y departamentos.
Incluye operaciones completas de CRUD.

Puede conectarse a:
SQLite (por defecto)
PostgreSQL (mediante variables de entorno)

Tecnologías utilizadas:
FastAPI
SQLModel
PostgreSQL
SQLite
Docker
Uvicorn

Estructura del proyecto:
app/
├── models
├── schemas
├── services
├── routers
├── db
└── main.py

Variables de entorno:
La aplicación admite configuración mediante variables de entorno:

Variable	Descripción:
DATABASE_URL	URL de conexión a base de datos
DEBUG	Activa modo debug
