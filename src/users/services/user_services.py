import sqlalchemy.orm as _orm


import src.users.config.user_config as _database
import src.users.schemas.user_schemas as _schemas
import src.users.models.user_models as _models

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def sign_in(db: _orm.Session, user: _schemas.User_SignIn):
    recieved_user =  db.query(_models.User).filter(_models.User.username==user.username).first() 
    if recieved_user.verify_password(user.password):
        return recieved_user

def register(db: _orm.Session, user: _schemas.UserCreate):
    user_obj = _models.User(**user.dict())
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

def get_user_info(db: _orm.Session, api_key: str):
    user = db.query(_models.User).filter(_models.User.api_key == api_key).first()
    if user:
       return user.api_key 
