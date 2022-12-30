from Controllers.Misc.genUser import GeneratedUser
from Controllers.Misc.misc import Misc
from flask import Response
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