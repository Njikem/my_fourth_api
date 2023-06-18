from flask import Flask,request
import dbhelpers, apihelpers
import json
import uuid

app = Flask(__name__)


@app.post("/api/client")
def post_clent():
    error = apihelpers.check_endpoint_info(request.json, ["username", "password"])
    if(error != None):
       return error
    results = dbhelpers.run_procedure("call get_two_clent(?,?)", [request.json.get("username"), request.json.get("password")])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "something went wrong, sorry"
    

@app.post("/api/login")
def post_login():
    error = apihelpers.check_endpoint_info(request.json, ["username", "password"])
    if(error != None):
       return error
    token = uuid.uuid4().hex
    results = dbhelpers.run_procedure("call get_login(?,?)", [request.json.get("username"), request.json.get("password"), token])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "something went wrong, sorry"
    

@app.post("/api/post")
def post_on_post():
    error = apihelpers.check_endpoint_info(request.json, ["token", "content"])
    if(error != None):
       return error
    token = uuid.uuid4().hex
    results = dbhelpers.run_procedure("call new_post(?,?)", [request.json.get("token"), request.json.get("content")])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "something went wrong, sorry"

