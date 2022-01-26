from models.dbconn import Base
from sqlalchemy import Column, String, Integer, DateTime, Text
from datetime import datetime


class Log(Base):
    __tablename__ = "log"

    logid = Column("logid", Integer, primary_key=True, autoincrement=True)
    userid = Column("userid", Integer)
    path = Column("path", String(100))
    method = Column("method", String(50))
    browser = Column("browser", String(50))
    browser_version = Column("browser_version", String(50))
    os = Column("os", String(50))
    ip_address = Column("ip_address", String(60))
    params = Column("params", Text)
    body = Column("body", Text)
    status = Column("status", Integer)
    duration = Column("duration", Integer)
    inserted_time = Column("inserted_time", DateTime)

    def __init__(
        self,
        userid="",
        path="",
        method="",
        browser="",
        browser_version="",
        os="",
        ip_address="",
        params="",
        body="",
        status=0,
        duration=1,
    ):
        self.userid = userid
        self.path = path
        self.method = method
        self.browser = browser
        self.browser_version = browser_version
        self.os = os
        self.ip_address = ip_address
        self.params = params
        self.body = body
        self.status = status
        self.duration = duration
        self.inserted_time = datetime.utcnow()
