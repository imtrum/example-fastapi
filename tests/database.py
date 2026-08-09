from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.main import app
from app.config import settings
from urllib.parse import quote_plus
from app.database import get_db, Base
import pytest
from app import models
# from alembic import command
# from alembic.config import Config


user = settings.database_username
password =settings.database_password
host = settings.database_hostname
port = settings.database_port
db_name = settings.database_name

safe_password = quote_plus(password)

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{user}:{safe_password}@{host}:{port}/{db_name}_test"
)
### break line
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine) 
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



# alembic_cfg = Config("alembic.ini")
@pytest.fixture()
def client(session):
    
    # command.downgrade(alembic_cfg,"base")
    # command.upgrade(alembic_cfg,"head")
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
            
    yield TestClient(app)