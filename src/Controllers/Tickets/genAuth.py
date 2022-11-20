from Controllers.Elements import xml
from Controllers.Database.User import *
from Crypto.Hash import SHA1
import datetime

class Ticket:
    def genAuth(self,user):
        # dt = datetime.now()
        h = SHA1.new()
        h.update(user.encode("utf-8"))
        h.update("test".encode("utf-8"))
        cookie = f"{user}:{str(h.hexdigest())}"
        auth = xml.Element.createElem("authTicket",f"MM_AUTH={cookie}")\
            +xml.Element.createElem("lbpEnvVer","ctbx DEV TEST")
        
        # setCookie = Users.select(username=user)
        # setCookie.authCookie = auth
        # setCookie.save()
        q = (Users
            .update({Users.authCookie:cookie})
            .where(Users.username == user)
            )
        q.execute()
        return auth