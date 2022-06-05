from flask import request, jsonify
from flask_restx import Resource, fields, reqparse
from werkzeug.datastructures import FileStorage
from service.Validatefunction import validateParamsFromCheckList
from flask_jwt_extended import jwt_required, get_jwt_identity
from swaggerConfig import api
from service.employees.getEmployees import GetEmployees
from service.employees.putEmployee import PutEmployee
from service.employees.getEmployeeDetail import GetEmployeeDetail

employee = api.namespace("employee", description="Post Apis")

get_employee_model= reqparse.RequestParser()

get_employee_with_id = reqparse.RequestParser()


get_employee_with_id = reqparse.RequestParser()
get_employee_with_id.add_argument(
    "EMPLOYEE_ID", type=str, required=True, help="unique name of user", location="args"
)

put_employee_model = reqparse.RequestParser()
put_employee_model.add_argument(
    "EMPLOYEE_ID", type=str, required=True, help="unique name of user", location="form"
)
put_employee_model.add_argument(
    "MANAGER_ID", type=str, help="unique name of user", location="form"
)
put_employee_model.add_argument(
    "DESIGNATION", type=str, required=True, help="unique name of user", location="form"
)
put_employee_model.add_argument(
    "DEPARTMENT", type=str, required=True, help="unique name of user", location="form"
)
put_employee_model.add_argument(
    "NAME", type=str, required=True, help="unique name of user", location="form"
)


@employee.route("/")
class Detail(Resource):
    # @jwt_required()
    @api.doc(responses={200: "OK"})
    @api.expect(get_employee_model)
    def get(self):
        output = GetEmployees()
        return jsonify(output)

    @api.doc(responses={200: "OK"})
    @api.expect(put_employee_model)
    def post(self):
        request_body= validateParamsFromCheckList(request.form, ["EMPLOYEE_ID", "NAME", "DEPARTMENT", "DESIGNATION", "MANAGER_ID"])
        output = PutEmployee(request_body)
        return jsonify(output)



@employee.route("/with/")
class SingleEmployee(Resource):
    # @jwt_required()
    @api.doc(responses={200: "OK"})
    @api.expect(get_employee_with_id)
    def get(self):
        request_body = validateParamsFromCheckList(request.args, ["EMPLOYEE_ID"])
        output = GetEmployeeDetail(request_body)
        return jsonify(output)
