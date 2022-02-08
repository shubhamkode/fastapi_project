import fastapi as _fastapi
import sqlalchemy.orm as _orm

import src.users.schemas.user_schemas as _schemas
import src.users.services.user_services as _services


router = _fastapi.APIRouter(prefix="/user",tags=["USER"])

_services.create_database()

@router.post("/sign_in",response_model=_schemas.User)
def sign_in(
    user: _schemas.User_SignIn, 
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    return _services.sign_in(db=db, user=user)

@router.post("/register", response_model=_schemas.User)
def registeration(
    user: _schemas.UserCreate, 
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    return _services.register(user=user, db=db)
