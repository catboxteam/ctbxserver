
from Controllers.Database.User import Users
from Controllers.Database.Slot import HeartedSlots,Slots
from Controllers.Misc.genSlot import Slotsx
from Controllers.Elements.xml import Element
from flask import request,Response
from Controllers.Misc.misc import *
from Controllers.Database.Queue import Queue
from Controllers.Misc.misc import Misc
import xml.etree.ElementTree as ET
from __main__ import app
import io 

#wtf
@app.route(f"{Misc.root}/lolcatftw/add/user/<slotId>",methods=["POST"])
@Misc.lbpRequest
def addlolcat(slotId):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()
    
    q = Queue(playerId=User.id,slotId=slotId)
    # q.slotId = slotId
    q.save()
    return Response(status=200)



@app.route(f"{Misc.root}/favouriteSlots/<user>",methods=["GET"])
@Misc.lbpRequest
def getFav(user):
    pageStart = int(request.args.get("pageStart"))-1
    pageSize = request.args.get("pageSize")

    getFav = (HeartedSlots.select().where(HeartedSlots.playerId==Misc.playerToId(user)))
    f =''
    for i in getFav.objects():
        f += Slotsx.genSlot("id",i.slotId,pageSize,pageStart)
    dd = Element.taggedElem2("favouriteSlots","total","hint_start",122,122,f)



    return Response(response=dd, status=200, mimetype="application/xml")

@app.route(f"{Misc.root}/favourite/slot/user/<ids>",methods=["POST"])
@Misc.lbpRequest
def setFav(ids):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()
    Slot = (Slots
    .update({Slots.heartCount: Slots.heartCount+1})
    .where(Slots.id==ids))
    
    d = HeartedSlots()
    d.playerId = User.id
    d.slotId = ids
    Slot.execute()
    d.save()

    return Response(status=200)

@app.route(f"{Misc.root}/unfavourite/slot/user/<ids>",methods=["POST"])
@Misc.lbpRequest
def unFav(ids):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()
    Slot = (Slots
    .update({Slots.heartCount: Slots.heartCount-1})
    .where(Slots.id==ids))
    d = HeartedSlots.delete().where(HeartedSlots.slotId==ids).where(HeartedSlots.playerId==User.id)
    
    d.execute()
    Slot.execute()
    return Response(status=200)