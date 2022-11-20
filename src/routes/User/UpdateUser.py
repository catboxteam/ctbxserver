root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users
from Controllers.Elements import xml
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import io

@app.route(f'{root}/updateUser',methods=['POST'])
def Update():
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()

    data = request.stream.read().decode()
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()
    for c in root:
        match c.tag:
            case "location":
                User.locationX = c.find("x").text
                User.locationY = c.find("y").text
            case "biography":
                User.biography = c.text
            case "icon":
                User.icon = c.text
            case "planets":
                User.planets = c.text
            case _:
                print(f"Tag not found ",c.tag,c.text)
                return Response(status=404)
        User.save()
    # print(User.authCookie)
    return Response(status=200)


@app.route(f'{root}/filterResources',methods=['POST'])
def filter():
    data = request.data.decode()
    print(data)
    return Response(status=200)

@app.route(f'{root}/showNotUploaded',methods=["POST"])
def notUploaded():
    return Response(request.data.decode(),status=200, mimetype='text/xml')
