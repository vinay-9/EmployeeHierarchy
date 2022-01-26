from dataclasses import asdict
from enum import unique
from flask_jwt_extended.utils import get_jwt_identity
from sqlalchemy.orm import relation
from models.dbconn import Session
from models.entities import Employee
from service.JsonResponse import JsonResponse
from sqlalchemy import and_, select, desc
import logConfig

def GetEmployeeDetail(req_obj):
    response = JsonResponse()
    session = Session()

    try:
        data= []
        employee = (
            session.query(
                Employee, 
            ).filter(
                 and_(
                    Employee.EMPLOYEE_ID== req_obj.get('EMPLOYEE_ID')
                )
            )
            .first()
        )
        session.add(employee)
        print(employee.manager)
        print(employee.reportees)
        # data = [
        # {
        #     "employee":{**asdict(row),
        #                 "reportees": [
        #                     getEmployeeData(reportees)
        #                     for reportee in row.reportees]}
        #     for row in employee}]
        if employee.reportees is not None:
            data= getEmployeeData(employee)
        else:
            data= {
            "employee":{**asdict(employee)}
            }

        response.set_data(data)
        session.commit()
        response.set_status(200)

    except Exception as e:
        response.set_status(500)  # Internal error
        response.set_message("Internal Server Error")
        response.set_error("Error in  fetching a profile => " + str(e))
        logConfig.logError("Error in  fetching a profile  => " + str(e))
    finally:
        session.close()
        return response.returnResponse()

def getEmployeeData(employee):
    return {
            "employee":{**asdict(employee),
                        "reportees": 
                          [ getEmployeeData(reportee)
                            for reportee in employee.reportees if employee.reportees is not None
                            ]
                    }
        }


# def getEmployeeData(employee):
#     return [{
#             "employee":{**asdict(row),
#                         "reportees": 
#                            {getEmployeeData(reportee)
#                             for reportee in row.reportees}
#                     }
#             for row in employee
#         }]