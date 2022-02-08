import sqlalchemy as _sql
import secrets

import src.users.config.user_config as _database


class User(_database.Base):
    __tablename__="users"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String)
    username=_sql.Column(_sql.String,unique=True)
    email=_sql.Column(_sql.String,unique=True)
    password=_sql.Column(_sql.String)
    api_key=_sql.Column(_sql.String, default=secrets.token_urlsafe(16))

    def verify_password(self,password: str):
        return self.password == password


