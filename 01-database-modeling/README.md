# 🧠 Módulo 01 — Modelado de Base de Datos

Este módulo forma parte del proyecto **SaaS Lab: Aprendizaje Modular Ético**. Aquí se aprende a modelar una base de datos relacional usando SQLAlchemy, con operaciones CRUD básicas y validación paso a paso.

## 🎯 Objetivo

- Aprender a definir modelos con SQLAlchemy
- Crear una base de datos SQLite para pruebas
- Implementar funciones CRUD (crear, leer, actualizar, eliminar)
- Validar cada operación desde un script de prueba

## 🧰 Tecnologías usadas

- **Lenguaje:** Python
- **ORM:** SQLAlchemy
- **Base de datos:** SQLite (modo local)
- **Testing manual:** `main.py`

## 📁 Estructura del módulo
01-db-modeling/ ├── database.py       # Conexión a la base de datos ├── models.py         # Definición de modelos (User) ├── crud.py           # Funciones CRUD ├── main.py           # Script de prueba ├── README.md         # Documentación del módulo


## 🧪 Cómo probar

1. Instalar dependencias:
   ```bash
   pip install sqlalchemy
2. Ejecutar el script:

   python main.py

3. Resultado esperado:
- Se crea el archivo test.db
- Se crea un usuario y se listan todos los usuarios en consola
📦 Funciones implementadas- create_user(db, name, email)
- get_all_users(db)
- update_user(db, user_id, new_email)
- delete_user(db, user_id)
🧠 Aprendizajes clave- Cómo usar declarative_base para definir modelos
- Cómo crear y cerrar sesiones con SessionLocal
- Cómo ejecutar operaciones CRUD con SQLAlchemy
- Cómo validar cada paso con scripts simples
