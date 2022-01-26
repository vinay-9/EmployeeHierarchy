from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = "localhost"
port = "3306"
username = "root"
password = "root"
db_name = "personal"


engine = create_engine(
    "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
        username, password, host, port, db_name
    ),
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
