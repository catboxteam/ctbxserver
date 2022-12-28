from Controllers.Elements import xml
from Controllers.Database.User import *
import secrets

class Ticket:
    def genAuth(self,user):
        # dt = datetime.now()

        cookie = f"{user}:{secrets.token_hex(25)}"
        auth = xml.Element.createElem("authTicket",f"MM_AUTH={cookie}")+xml.Element.createElem("lbpEnvVer","ctbxserver")
        
        # setCookie = Users.select(username=user)
        # setCookie.authCookie = auth
        # setCookie.save()
        # q = (Users
        #     .update({Users.authCookie:cookie})
        #     .where(Users.username == user)
        #     )

        q = Users.select().where(Users.username==user).get()

        q.authCookie = cookie
        q.save()
        return auth