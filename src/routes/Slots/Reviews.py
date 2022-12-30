
from Controllers.Database.Slot import Slots
from Controllers.Database.User import Users
from Controllers.Elements.xml import Element
from Controllers.Misc.genSlot import Slotsx
from Controllers.Database.Review import Reviews
from Controllers.Misc.misc import Misc
from flask import request,Response
from Controllers.Misc.misc import *
import xml.etree.ElementTree as ET
from __main__ import app
import io 

#postReview/user/slotId
# <review>
#   <thumb>1</thumb>
#   <labels>LABEL_Quick</labels>
#   <text>Good level! </text>
# </review>

#review id="SLOTID.username"

def gen(id):
    q = (Reviews
    .select()
    .where(Reviews.id==id))

    f = ''
    final = ''
    for i in q:
        f += Element.taggedElem("slot_id","type","user",i.slotId)
        f += Element.createElem("reviewer",Misc.idToPlayer(i.playerId))
        f += Element.createElem("thumb",i.thumb)
        f += Element.createElem("timestamp",i.thumb)
        f += Element.createElem("deleted",i.deleted)
        f += Element.createElem("deleted_by",i.deletedBy)
        f += Element.createElem("labels",i.labels)
        f += Element.createElem("text",i.text)
        f += Element.createElem("thumbsup",i.thumbsup)
        f += Element.createElem("thumbsdown",i.thumbsdown)

        final += Element.taggedElem("review","id",f"{i.slotId}.{Misc.idToPlayer(i.playerId)}",f)

    return final



@app.route(f"{Misc.root}/postReview/user/<slotId>",methods=["POST"])
@Misc.lbpRequest
def createReview(slotId):
    cookie = request.cookies.get("MM_AUTH")
    user = Users.select().where(Users.authCookie == cookie).get().id
    data = request.data.decode()
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()
    

    review, created = Reviews.get_or_create(playerId=user, slotId=slotId)
    review.timestamp = Misc.timestamp()

    for c in root:
        tag = c.tag
        text = c.text
        if tag == "thumb":
            review.thumb = text
        elif tag == "labels":
            review.labels = text
        elif tag == "text":
            review.text = text
    review.save()
    return Response(status=200)


@app.route(f"{Misc.root}/reviewsFor/user/<slotid>",methods=["GET"])
@Misc.lbpRequest
def rev(slotid):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get().id
    c = (Reviews
        .select()
        .where(Reviews.slotId==slotid))



    
    if c.where(Reviews.playerId==User).exists():
        f = ''
    else:
        f = f"""
        <review id="{slotid}.{Misc.idToPlayer(User)}">
            <slot_id type="user">{slotid}</slot_id>
            <reviewer>{Misc.idToPlayer(User)}</reviewer>
            <thumb>1</thumb>
            <timestamp>1343916636355</timestamp>
            <deleted>false</deleted>
            <deleted_by>none</deleted_by>
            <text>Edit to post review</text>
            <thumbsup>0</thumbsup>
            <thumbsdown>0</thumbsdown>
            <yourthumb>0</yourthumb>
        </review>"""

    for i in c:
        f += gen(i.id)

    rev = Element.createElem("reviews",f)

    print("test")
    return Response(rev,status=200, mimetype='text/xml') 


@app.route(f"{Misc.root}/reviewsBy/<username>",methods=["GET"])
@Misc.lbpRequest
def revBy(username):
    c = (Reviews
        .select()
        .where(Reviews.playerId==Misc.playerToId(username)))
    f =''
    for i in c:
        f += gen(i.id)

    rev = Element.createElem("reviews",f)

    print("test")
    return Response(rev,status=200, mimetype='text/xml') 
