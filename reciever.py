from flask import Blueprint
from flask_cors import cross_origin

info_api = Blueprint("get_api", __name__)

@info_api.route("/api/v1/info", methods=["GET"])
@cross_origin()
def info():
    return {"Receiver": "Cisco is the best!"}