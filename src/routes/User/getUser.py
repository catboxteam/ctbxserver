root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.User import Users
from Controllers.Elements import xml
from flask import request,Response
from __main__ import app

@app.route(f'{root}/user/<name>',methods=['GET'])
def getUser(name):
    try:
        xmls = xml.Element

        user = Users.get(username=name)
        location = xmls.createElem("x",user.locationX)\
            +xmls.createElem("y",user.locationY)
        finalResult = xmls.createElem("location",location)

        final = xmls.taggedElem("npHandle","icon",user.iconHash,user.username)
        final += xmls.createElem("game","2")
        final += xmls.createElem("lbp1UsedSlots","0")
        final += xmls.createElem("entitledSlots","50")
        final += xmls.createElem("freeSlots","50") #AllSlots - usedSlots\

        final += xmls.createElem("crossControlUsedSlots","0")
        final += xmls.createElem("crossControlEntitledSlots","50")
        final += xmls.createElem("crossControlPurchasedSlots","0")
        final += xmls.createElem("crossControlFreeSlots","50")

        final += xmls.createElem("lbp2UsedSlots","0")
        final += xmls.createElem("lbp2EntitledSlots","50")
        final += xmls.createElem("lbp2PurchasedSlots","0")
        final += xmls.createElem("lbp2FreeSlots","50")

        final += xmls.createElem("lbp3UsedSlots","0")
        final += xmls.createElem("lbp3EntitledSlots","50")
        final += xmls.createElem("lbp3PurchasedSlots","0")
        final += xmls.createElem("lbp3FreeSlots","50")

        final += xmls.createElem("lists_quota","50")
        final += xmls.createElem("heartCount",user.heartCount)
        final += xmls.createElem("planets",user.planetHash)
        final += xmls.createElem("crossControlPlanet",user.planetHash)
        final += xmls.createElem("yay2",user.yayHash)
        final += xmls.createElem("boo2",user.booHash)
        final += xmls.createElem("meh2",user.booHash)
        final += xmls.createElem("biography",user.biography)
        final += xmls.createElem("reviewCount",user.reviewCount)
        final += xmls.createElem("commentCount",user.commentsCount)

        final += xmls.createElem("photosByMeCount","0")
        final += xmls.createElem("photosWithMeCount","0")

        final += xmls.createElem("commentsEnabled",user.commentsEnabled)
        final += finalResult
        final += xmls.createElem("favouriteSlotCount",user.heartedSlots)
        final += xmls.createElem("favouriteUserCount",user.heartedAuthors)

        final += xmls.createElem("pins",user.pins)

        finalUser = xmls.taggedElem("user","type","user",final)
        return Response(finalUser,status=200, mimetype='text/xml')
    except Exception as e:
        return Response(e,status=404)









        









    except Exception as e:
        print(e)