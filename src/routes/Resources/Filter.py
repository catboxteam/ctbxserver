root = "/LITTLEBIGPLANETPS3_XML"
from flask import request,Response
from __main__ import app
@app.route(f"{root}/filter",methods=["POST"])
def filters():
    return request.data.decode()