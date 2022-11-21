root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users
from Controllers.Database.Slot import HeartedSlots,Slots
from Controllers.Misc.genSlot import Slotsx

from Controllers.Elements.xml import Element
from Controllers.Misc.misc import Misc
from flask import request,Response
from Controllers.Misc.misc import *
import xml.etree.ElementTree as ET
from __main__ import app
import io 

@app.route(f"{root}/favouriteSlots/<user>",methods=["GET"])
def getFav(user):
    pageStart = int(request.args.get("pageStart"))-1
    pageSize = request.args.get("pageSize")

    getFav = (HeartedSlots.select().where(HeartedSlots.username==user))
    f =''
    for i in getFav.objects():
        f += Slotsx.genSlot("id",i.slotId,pageSize,pageStart)
    dd = Element.taggedElem2("favouriteSlots","total","hint_start",122,122,f)



    return Response(response=dd, status=200, mimetype="application/xml")

@app.route(f"{root}/favourite/slot/user/<ids>",methods=["POST"])
def setFav(ids):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()
    Slot = (Slots
    .update({Slots.heartCount: Slots.heartCount+1})
    .where(Slots.id==ids))
    d = HeartedSlots()

    d.username = User.username
    d.slotId = ids
    Slot.execute()
    d.save()

    return Response(status=200)
