root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users
from Controllers.Database.Comment import Comments
from Controllers.Misc.misc import Misc
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import io

@app.route(f'{root}/postUserComment/<name>',methods=['POST'])
def postComment(name):
    cookie = request.cookies.get("MM_AUTH")
    data = request.stream.read().decode()
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()

    misc = Misc

    for c in root:
        match c.tag:
            case "message":
                User = Users.select().where(Users.username == name).get()
                Comments.create(
                    username=Users.select().where(Users.authCookie == cookie).get().username,
                    message=c.text,
                    timestamp=misc.timestamp(),
                    toUser=name
                    )
                User.commentsCount += 1
                User.save()

    return Response(status=200)
