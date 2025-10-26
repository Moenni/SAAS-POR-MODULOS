from sqlalchemy.orm import Session
from models import User

#CREACION DE USUARIO
def create_user(db: Session, name:str, email:str):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#ACTUALIZACION DE USUARIO
def update_user(db:Session,user_id:int,new_email:str):
    user=db.query(User).filter(User.id==user_id).first()
    if user:
        user.email=new_email
        db.commit()
        db.refresh(user)
    return user

#ELIMINACION DE USUARIO
def delete_user(db:Session,user_id:int):
    user=db.query(User).filter(User.id==user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

#LECTURA DE USUARIOS
def get_all_users(db: Session):
    return db.query(User).all()
