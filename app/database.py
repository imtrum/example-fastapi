from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


user = settings.database_username
password =settings.database_password
host = settings.database_hostname
port = settings.database_port
db_name = settings.database_name

safe_password = quote_plus(password)

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{user}:{safe_password}@{host}:{port}/{db_name}"
)
### break line
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while  True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='hanHuuduong@111', cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)