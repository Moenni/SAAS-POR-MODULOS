from database import engine
from models import Base
from database import SessionLocal
from crud import create_user, get_all_users
import time

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Crear un nuevo usuario con email único (usando timestamp)
timestamp = int(time.time())
user = create_user(db, name="Alice", email=f"alice{timestamp}@borderlands.com")
print("Usuario creado exitosamente:", user.name, user.email)

#listar todos los usuarios

users=get_all_users(db)
print("Usuarios Creados en DB:")
for u in users:
    print(u.id,u.name,u.email)