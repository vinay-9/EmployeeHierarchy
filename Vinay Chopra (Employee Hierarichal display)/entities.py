from datetime import datetime
from enum import Enum

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.ext.associationproxy import association_proxy
from models.dbconn import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    DateTime,
    BigInteger,
    ForeignKey,
    Enum,
    select,
)
from dataclasses import dataclass
from sqlalchemy import func



@dataclass
class Employee(Base):
    __tablename__ = "employee"
    SNO: int
    EMPLOYEE_ID: str
    DESIGNATION: str
    DEPARTMENT: str
    NAME: str
    MANAGER_ID: str


    SNO = Column("SNO", BigInteger, autoincrement=True)
    EMPLOYEE_ID = Column("EMPLOYEE_ID", String(255), primary_key= True)
    DESIGNATION= Column ("DESIGNATION", String(255), nullable=True)
    DEPARTMENT= Column ("DEPARTMENT", String(255), nullable=True)
    NAME= Column ("NAME", String(255), nullable=True)
    MANAGER_ID= Column ("MANAGER_ID", String(255), ForeignKey("employee.EMPLOYEE_ID"))
    reportees = relationship("Employee",
                backref=backref('manager', remote_side=[EMPLOYEE_ID])
            )

   
    def __repr__(self):
        return "<Employee SNO={0} EMPLOYEE_ID= {1}>".format(self.SNO, self.EMPLOYEE_ID)

