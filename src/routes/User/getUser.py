from Controllers.Misc.misc import Misc

from Controllers.Database.User import Users,heartedUser
from Controllers.Database.Slot import Slots,HeartedSlots
from Controllers.Database.Photo import UserPhoto
from Controllers.Misc.genUser import GeneratedUser

from Controllers.Database.Comment import Comments

from Controllers.Elements.xml import Element
from flask import request,Response
from __main__ import app

@app.route(f'{Misc.root}/user/<name>',methods=['GET'])
def getUser(name):
    try:
        t = GeneratedUser.genUsr(name)
        return Response(t,status=200, mimetype='text/xml')
    except Exception as e:
        return Response(e,status=404)

#shut up
@app.route(f'{Misc.root}/privacySettings',methods=['GET'])
def Settings():
    return Response("<privacySettings><levelVisibility>all</levelVisibility><profileVisibility>all</profileVisibility></privacySettings",status=200)