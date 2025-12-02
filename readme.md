

# 🎓 Sistema de Notas – Backend (FastAPI)

API del Sistema de Notas Académico con módulos `Admin`, `Docente` y `Estudiante`.

## Requisitos

- `Python >= 3.10`
- `PostgreSQL >= 12`

## Instalación local

- Crear entorno: `python -m venv .venv && .venv\Scripts\activate`
- Instalar dependencias: `pip install -r requirements.txt`
- Crear BD y credenciales en PostgreSQL.

## Variables de entorno

Editar `.env`:

```
# Base de datos
DATABASE_URL=postgresql+psycopg://usuario:password@localhost:5432/sistema_notas

# JWT
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=120

# CORS (incluye dominios del frontend en https)
CORS_ORIGINS=["http://localhost:5173","https://clientnotas-production.up.railway.app"]

# Email (recuperación de contraseña)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu_email
SMTP_PASSWORD=tu_password_aplicacion

# Proxy (recomendado en producción)
FORWARDED_ALLOW_IPS=*
```

## Ejecutar en desarrollo

- `uvicorn main:app --host 0.0.0.0 --port 9001 --reload`
- Docs: `http://localhost:9001/docs` y `http://localhost:9001/redoc`

## Estructura

- `app/modules/admin`: Gestión de docentes, estudiantes, matrículas, cursos/ciclos y reportes.
- `app/modules/teacher`: Cursos, calificaciones, perfil y reportes del docente.
- `app/modules/student`: Dashboard, cursos, notas, perfil y horario del estudiante.
- `app/shared`: Modelos compartidos y utilidades.
- `main.py`: Carga de routers, CORS y `ProxyHeadersMiddleware`.
- `static/`: Archivos estáticos servidos en `/static`.

## Prefijos y endpoints

- Prefijo global: `/api/v1`.
- `Admin`: `/api/v1/admin/...`
- `Teacher`: `/api/v1/teacher/...`
- `Student`: `/api/v1/student/...`
- `Auth`: `/api/v1/auth/...`

Las rutas de lista usan `"/"` (p. ej. `/api/v1/admin/docentes/`). Consumirlas con `slash` final evita `307`.

## Despliegue en Railway

- `railway.json` inicia con: `uvicorn main:app --host 0.0.0.0 --port $PORT --proxy-headers`.
- Añadir `FORWARDED_ALLOW_IPS=*` para que Starlette confíe en headers del proxy.
- Asegurar `CORS_ORIGINS` que incluya el origen del frontend en `https`.

## HTTPS y Mixed Content

- El backend ahora añade `ProxyHeadersMiddleware` y se inicia con `--proxy-headers` para construir redirects en `https` detrás del proxy.
- El frontend debe usar `VITE_API_URL` en `https`. Si se usa `http`, el navegador bloquea las peticiones.

## Datos de prueba

- `python seeder.py` para crear datos iniciales.

## Solución de problemas

- `307 Temporary Redirect`: usa rutas con `slash` final en el cliente o valida que los redirects apunten a `https`.
- `Mixed Content`: verifica `VITE_API_URL` en `https` y configuración de proxy.
- `CORS`: agrega el origen del frontend en `CORS_ORIGINS`.
- `DB`: confirma `DATABASE_URL` y conectividad.
