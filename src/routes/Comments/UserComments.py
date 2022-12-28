
from Controllers.Database.User import Users
from Controllers.Database.Comment import Comments
from Controllers.Misc.misc import Misc
from Controllers.Elements.xml import Element
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import io
@app.route(f'{Misc.root}/postComment/user/<name>',methods=['POST'])
@app.route(f'{Misc.root}/postUserComment/<name>',methods=['POST'])
def postComment(name):
    cookie = request.cookies.get("MM_AUTH")
    usr = Users.select().where(Users.authCookie == cookie).get()
    print(usr.id)
    data = request.stream.read().decode()
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()

    misc = Misc

    for c in root:
        match c.tag:
            case "message":
                Comments.create(
                    playerId=usr.id,
                    message=c.text,
                    timestamp=misc.timestamp(),
                    toUser=name
                    )

    return Response(status=200)

@app.route(f'{Misc.root}/comments/user/<user>',methods=['GET'])
@app.route(f'{Misc.root}/userComments/<user>',methods=['GET'])
def getComments(user):

    pageStart = int(request.args.get("pageStart")) -1
    pageSize = int(request.args.get("pageSize"))


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
        ids = Element.createElem("id", r.id)
        ids += Element.createElem("npHandle", Misc.idToPlayer(r.playerId))
        ids += Element.createElem("timestamp", r.timestamp)
        ids += Element.createElem("message", r.message)
        ids += Element.createElem("yourthumb", 0)

        if r.isDeleted:
            ids += Element.createElem("deleted", "true")
            ids += Element.createElem("deletedBy", r.deletedUser)
            ids += Element.createElem("deleteType", r.deletedType)

        # if r.isDeleted == True:
        #     ids = Element.createElem("id",r.id)\
        #             +Element.createElem("npHandle",Misc.idToPlayer(r.playerId))\
        #             +Element.createElem("timestamp",r.timestamp)\
        #             +Element.createElem("message",r.message)\
        #             +Element.createElem("yourthumb",0)\
        #             +Element.createElem("deleted","true")\
        #             +Element.createElem("deletedBy",r.deletedUser)\
        #             +Element.createElem("deleteType",r.deletedType)
        # elif r.isDeleted == False:
        #     ids = Element.createElem("id",r.id)\
        #             +Element.createElem("npHandle",Misc.idToPlayer(r.playerId))\
        #             +Element.createElem("timestamp",r.timestamp)\
        #             +Element.createElem("message",r.message)\
        #             +Element.createElem("yourthumb",0)\

        comment += Element.createElem("comment",ids)

    comments1 = Element.createElem("comments",comment)
    return Response(response=comments1, status=200, mimetype="application/xml")


@app.route(f'{Misc.root}/deleteUserComment/<user>',methods=['POST'])
@app.route(f'{Misc.root}/deleteComment/user/<user>',methods=['POST'])
def deleteComments(user):
    cookie = request.cookies.get("MM_AUTH")
    user =  Users.select().where(Users.authCookie == cookie).get().username

    #'user' is owner of comment or??
    
    commentId = int(request.args.get("commentId"))
    
    comment = Comments.get_by_id(commentId)
    comment.isDeleted = True
    comment.deletedType = "user"
    comment.deletedUser = user
    comment.save()

    return Response(status=200)



@app.route(f'{Misc.root}/rateComment/user/<slotId>',methods=['POST'])
def rateComment(slotId):
    commentId = request.args.get("commentId")
    rating = request.args.get("rating")
    print(commentId,rating)
    return Response(status=200)
