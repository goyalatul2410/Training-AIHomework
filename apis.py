from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests

health_api = Blueprint("health_api", __name__)
ping_api = Blueprint("ping_api", __name__)

@health_api.route("/health", methods=["GET"])
@cross_origin()
def health():
    return {"health": "healthy"}


@ping_api.route("/api/v1/ping", methods=["POST"])
@cross_origin()
def ping():
    request_url = json.loads(request.get_data())
    
    res =  requests.get(url=request_url["url"])

    api_result = res.json()

    return api_result
