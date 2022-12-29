from Controllers.Database.User import Users,heartedUser
from functools import wraps
from datetime import datetime
import time
import os.path


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


