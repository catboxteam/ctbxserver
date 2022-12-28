

from Controllers.Database.User import Users,heartedUser
from Controllers.Misc.genUser import GeneratedUser
from Controllers.Elements.xml import Element
from Controllers.Misc.misc import Misc
from Controllers.Elements import xml
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import json
import io

@app.route(f'{Misc.root}/favourite/user/<username>',methods=['POST'])
def Favourite(username):

    cookie = request.cookies.get("MM_AUTH")

    User = Users.select().where(Users.authCookie == cookie).get()
    d = heartedUser(playerId=Misc.playerToId(username))
    d.playerId = Misc.playerToId(username)
    d.whoHearted = User.username
    d.save()

    return Response(status=200)

#<favouriteUsers total="3" hint_start="4">

#</favouriteUsers>

@app.route(f'{Misc.root}/favouriteUsers/<usernames>',methods=['GET'])
def getList(usernames):
    q = (heartedUser.select().where(heartedUser.whoHearted==usernames))
    totalUsers =''
    for i in q:
        totalUsers += GeneratedUser.genUsr(Misc.idToPlayer(i.playerId))

    dd = Element.taggedElem2("favouriteUsers","total","hint_start",122,122,totalUsers)
    
    return Response(dd,status=200, mimetype='text/xml')

@app.route(f'{Misc.root}/unfavourite/user/<usernames>',methods=['POST'])
def unfav(usernames):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()
    d = heartedUser.delete().where(heartedUser.playerId==Misc.playerToId(usernames)).where(heartedUser.whoHearted==User.username)
    d.execute()
    return Response(status=200)
