import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy as _sql


DATABASE_URL = 'postgresql+psycopg2://postgres:password@localhost:5432/todo'

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
