from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from urllib.parse import urlsplit, urlunsplit

# Crear el engine de la base de datos
_url = settings.database_url
if _url.startswith("postgresql://"):
    parts = urlsplit(_url)
    _url = urlunsplit(("postgresql+psycopg", parts.netloc, parts.path, parts.query, parts.fragment))
engine = create_engine(_url)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()