from Controllers.Misc.Info import ServerInfo
from Controllers.Database.User import Users
from flask import request,Response
from datetime import datetime
from functools import wraps
import hashlib
import os.path
import time


class Misc:
    
    root = "/LITTLEBIGPLANETPS3_XML"

    def checkFile(hash):
        return os.path.exists(f"r/{hash}")

    def timestamp():
        millisecond = datetime.now()
        timez = time.mktime(millisecond.timetuple()) * 1000
        return timez

    def idToPlayer(id):
        f = Users.select(Users.username).where(Users.id==id).execute()
        return f[0].username
    
    def playerToId(username):
        f = Users.select(Users.id).where(Users.username==username).execute()
        return f[0].id


    def lbpRequest(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cookie = request.cookies.get("MM_AUTH")
            sha1Digest = request.headers.get('x-digest-a')
            if cookie and sha1Digest and ServerInfo.digestKey:
                m = hashlib.sha1()
                m.update(request.data)
                m.update(request.cookies.get("MM_AUTH").encode('utf-8'))
                m.update(request.path.encode('utf-8'))
                m.update(str(ServerInfo.digestKey).encode('utf-8'))
                if sha1Digest == m.hexdigest():
                    return f(*args, **kwargs)
                else:
                    # print(f'From headers: {sha1Digest} | computed: {m.hexdigest()}')
                    return Response(status=403,response="Invalid digest!")
            else:
                return Response(status=403,response="Not LittleBigPlanet request!")

        return decorated_function