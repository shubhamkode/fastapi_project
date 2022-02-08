import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    name: str
    email: _pydantic.EmailStr

class UserCreate(_UserBase):
    username: str
    password: str

class User(_UserBase):
    id: int
    api_key: str
    class Config:
        orm_mode=True

class User_SignIn(_pydantic.BaseModel):
    username: str
    password: str


