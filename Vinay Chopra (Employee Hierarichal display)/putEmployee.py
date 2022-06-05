from dataclasses import asdict
from enum import unique
from flask_jwt_extended.utils import get_jwt_identity
from sqlalchemy.orm import relation
from models.dbconn import Session
from models.entities import  Employee
from service.JsonResponse import JsonResponse
from sqlalchemy import and_, select, desc
import logConfig


def PutEmployee(req_obj):
    response = JsonResponse()
    session = Session()

    try:
        
        employee=Employee(
            EMPLOYEE_ID=req_obj.get('EMPLOYEE_ID'),
            DEPARTMENT=req_obj.get('DEPARTMENT'),
            DESIGNATION=req_obj.get('DESIGNATION'),
            MANAGER_ID=req_obj.get('MANAGER_ID'),
            NAME=req_obj.get('NAME'),
        )
        if req_obj.get('MANAGER_ID') is not None:
            
            manager_obj = (
                session.query(Employee)
                .filter(Employee.EMPLOYEE_ID == req_obj.get('MANAGER_ID'))
                .first()
            )   

            manager_obj.reportees.append(employee)
            employee.manager= manager_obj

            print("employee's manager",employee.manager)
            print({**asdict(employee.manager)})


        session.add(employee)
        session.add(manager_obj)
        print({**asdict(employee)})
        response.set_data( {"employee":{**asdict(employee)}, "manager": {**asdict(employee.manager)} })
        response.set_status(200)

        session.commit()
    except Exception as e:
        response.set_status(500)  # Internal error
        response.set_message("Internal Server Error")
        response.set_error("Error in  fetching a profile => " + str(e))
        logConfig.logError("Error in  fetching a profile  => " + str(e))
    finally:
        session.close()
        return response.returnResponse()
