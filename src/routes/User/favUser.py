root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users,heartedUser
from Controllers.Elements import xml
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import json
import io

@app.route(f'{root}/favourite/user/<username>',methods=['POST'])
def Favourite(username):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()

    d = heartedUser()
    d.username = username
    d.whoHearted = User.username
    d.save()

    return Response(status=200)