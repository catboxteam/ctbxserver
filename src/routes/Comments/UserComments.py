root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users
from Controllers.Database.Comment import Comments
from Controllers.Misc.misc import Misc
from Controllers.Elements import xml
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
                Comments.create(
                    username=Users.select().where(Users.authCookie == cookie).get().username,
                    message=c.text,
                    timestamp=misc.timestamp(),
                    toUser=name
                    )

    return Response(status=200)


@app.route(f'{root}/userComments/<user>',methods=['GET'])
def getComments(user):

    pageStart = int(request.args.get("pageStart")) -1
    pageSize = int(request.args.get("pageSize"))

    xmls = xml.Element

    comment = ''
    ids = ''

    comments = (Comments
    .select(Comments)
    .where(Comments.toUser==user)
    .order_by(Comments.timestamp.desc())
    .limit(pageSize)
    .offset(pageStart)
    # .paginate(pageStart, pageSize)
    )

    for r in comments:
        if r.isDeleted == True:
            ids = xmls.createElem("id",r.id)\
                    +xmls.createElem("npHandle",r.username)\
                    +xmls.createElem("timestamp",r.timestamp)\
                    +xmls.createElem("message",r.message)\
                    +xmls.createElem("yourthumb",0)\
                    +xmls.createElem("deleted",r.isDeleted)\
                    +xmls.createElem("deletedBy",r.deletedBy)\
                    +xmls.createElem("deleteType",r.deletedType)
        elif r.isDeleted == False:
            ids = xmls.createElem("id",r.id)\
                    +xmls.createElem("npHandle",r.username)\
                    +xmls.createElem("timestamp",r.timestamp)\
                    +xmls.createElem("message",r.message)\
                    +xmls.createElem("yourthumb",0)\

        comment += xmls.createElem("comment",ids)

    comments1 = xmls.createElem("comments",comment)
    return Response(response=comments1, status=200, mimetype="application/xml")