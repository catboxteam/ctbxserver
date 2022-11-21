root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users
from Controllers.Database.Slot import Slots

from Controllers.Database.Comment import Comments

from Controllers.Elements.xml import Element
from flask import request,Response
from __main__ import app

@app.route(f'{root}/user/<name>',methods=['GET'])
def getUser(name):
    try:
    
        comments = (Comments
            .select(Comments)
            .where(Comments.toUser==name)).count()


        # Slots = (Slots
        #     .select(Slots)
        #     .where(Slots.username==name).count()
        # )

        user = Users.get(username=name)
        location = Element.createElem("x",user.locationX)\
            +Element.createElem("y",user.locationY)
        finalResult = Element.createElem("location",location)

        final = Element.taggedElem("npHandle","icon",user.iconHash,user.username)
        final += Element.createElem("game","2")
        final += Element.createElem("lbp1UsedSlots","0")
        final += Element.createElem("entitledSlots","50")
        final += Element.createElem("freeSlots","50") #AllSlots - usedSlots\

        final += Element.createElem("crossControlUsedSlots","0")
        final += Element.createElem("crossControlEntitledSlots","50")
        final += Element.createElem("crossControlPurchasedSlots","0")
        final += Element.createElem("crossControlFreeSlots","50")

        final += Element.createElem("lbp2UsedSlots","0")
        final += Element.createElem("lbp2EntitledSlots","50")
        final += Element.createElem("lbp2PurchasedSlots","0")
        final += Element.createElem("lbp2FreeSlots","50")

        final += Element.createElem("lbp3UsedSlots","0")
        final += Element.createElem("lbp3EntitledSlots","50")
        final += Element.createElem("lbp3PurchasedSlots","0")
        final += Element.createElem("lbp3FreeSlots","50")

        final += Element.createElem("lists_quota","50")
        final += Element.createElem("heartCount",user.heartCount)
        final += Element.createElem("planets",user.planetHash)
        final += Element.createElem("crossControlPlanet",user.planetHash)
        final += Element.createElem("yay2",user.yayHash)
        final += Element.createElem("boo2",user.booHash)
        final += Element.createElem("meh2",user.booHash)
        final += Element.createElem("biography",user.biography)
        final += Element.createElem("reviewCount",user.reviewCount)
        final += Element.createElem("commentCount",comments)

        final += Element.createElem("photosByMeCount","0")
        final += Element.createElem("photosWithMeCount","0")

        final += Element.createElem("commentsEnabled",user.commentsEnabled)
        final += finalResult
        final += Element.createElem("favouriteSlotCount",user.heartedSlots)
        final += Element.createElem("favouriteUserCount",user.heartedAuthors)

        final += Element.createElem("pins",user.pins)

        finalUser = Element.taggedElem("user","type","user",final)
        return Response(finalUser,status=200, mimetype='text/xml')
    except Exception as e:
        return Response(e,status=404)