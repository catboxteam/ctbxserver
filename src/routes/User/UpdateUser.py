from Controllers.Misc.misc import Misc

from Controllers.Database.User import Users
from Controllers.Elements import xml
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import json
import io

@app.route(f'{Misc.root}/updateUser',methods=['POST'])
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
                User.iconHash = c.text
            case "planets":
                User.planetHash = c.text
            case "yay2":
                User.yayHash = c.text
            case "boo2":
                User.booHash = c.text
            case "meh2":
                User.mehHash = c.text       
            case _:
                print(f"Tag not found ",c.tag,c.text)
                return Response(status=404)
        User.save()
    # print(User.authCookie)
    return Response(status=200)


@app.route(f'{Misc.root}/update_my_pins',methods=['POST'])
def Pins():
    cookie = request.cookies.get("MM_AUTH")
    user = Users.select().where(Users.authCookie == cookie).get()
    f = json.loads(request.data.decode())
    pins = f["profile_pins"]
    parsed = ",".join(str(x) for x in pins)
    user.pins = parsed
    user.save()
    return Response(response="[{\"StatusCode\":200}]")

@app.route(f'{Misc.root}/filterResources',methods=['POST'])
def filter():
    data = request.data.decode()
    print(data)
    return Response(data,status=200)

@app.route(f'{Misc.root}/showNotUploaded',methods=["POST"])
def notUploaded():
    return Response(request.data.decode(),status=200, mimetype='text/xml')
