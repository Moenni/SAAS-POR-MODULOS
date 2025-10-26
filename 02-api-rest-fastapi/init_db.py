from database import Base, engine
from models import User

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Base de datos inicializada - tablas creadas.")

if __name__ == "__main__":
    init_db()