from swaggerConfig import app
import os
from models.dbconn import Base, engine
from flask import Flask, g, request
from flask_jwt_extended import JWTManager
from service.StoreLog import StoreLog
from flask_restx import Api
import time, datetime, os, json, decimal
from flask_jwt_extended import get_jwt_identity
import threading
import routes.route_employee


def initilize_db():
    from models.log import Log
    from models.entities import  Employee

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    initilize_db()
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    app.run(host="0.0.0.0", port=5001, debug=True)


def ServerLog(logObject):
    StoreLog().log(logObject)




