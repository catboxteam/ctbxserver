root = "/LITTLEBIGPLANETPS3_XML"
from flask import request,Response
from __main__ import app

@app.route(f"{root}/upload/<sha1>",methods=["POST"])
def Upload(sha1):
    try:
        open(f"r/{sha1}","wb").write(request.data)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=404)


@app.route(f"{root}/r/<sha1>",methods=["GET"])
def Read(sha1):
    try:
        return Response(response=open(f"r/{sha1}",'rb').read(),status=200)
    except Exception as e:
        print(e)
        return Response(status=404)
        
@app.route(f"{root}/showModerated",methods=["POST"])
def showModerated():
    return Response("</resources>",status=200)