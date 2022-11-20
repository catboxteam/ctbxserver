root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.Slot import Slots
from Controllers.Database.User import Users
from Controllers.Elements.xml import Element
from Controllers.Misc.genSlot import Slotsx
from Controllers.Misc.misc import Misc
from flask import request,Response
from Controllers.Misc.misc import *
import xml.etree.ElementTree as ET
from __main__ import app
import io 


@app.route(f"{root}/startPublish",methods=["POST"])
def startPublish():
    startPub = Misc.timestamp()

    data = request.stream.read().decode()
    cookie = request.cookies.get("MM_AUTH")
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()

    resources = []
    links = []

    dd = Slots(username=Users.select().where(Users.authCookie == cookie).get().username)
    dd.firstPublished =startPub
    dd.lastUpdated = startPub
    for child in root:
        match child.tag:
            case "name":
                name = child.text
                dd.name = child.text
            case "description":
                description = child.text
                dd.description = child.text
            case "icon":
                icon = child.text
                dd.icon = child.text
            case "rootLevel":
                rootL = child.text
                dd.rootLevel = child.text
            case "location":
                dd.locationX = child.find("x").text
                dd.locationY = child.find("y").text
            case "initiallyLocked":
                initiallyLocked = child.text
                dd.initiallyLocked = child.text
            case "isSubLevel":
                isSubLevel = child.text
                dd.isSubLevel = child.text
            case "isLBP1Only":
                isLBP1Only = child.text
                dd.isLBP1Only = child.text
            case "shareable":
                shareable = child.text
                dd.shareable = child.text
            case "authorLabels":
                authorLabels = child.text
                dd.authorLabels = child.text
            case "background":
                background = child.text
                dd.background = child.text
            case "links":
                print("todo")
                if child.find("id") == None:
                    pass
                else:
                    links.append(child.find("id").text)
                    linksParse = ';'.join(links)
                    dd.links = linksParse
            case "internalLinks":
                print("todo")
            case "leveltype":
                leveltype = child.text
                dd.leveltype = child.text
            case "minPlayers":
                minPlayers = child.text
                dd.minPlayers = child.text
            case "maxPlayers":
                maxPlayers = child.text
                dd.maxPlayers = child.text
            case "moveRequired":
                moveRequired = child.text
                dd.moveRequired = child.text
            case "resource":
                resources.append(child.text)
                resourceParse = ';'.join(resources)
                dd.resource = resourceParse
            case _:
                print(f"Not found {child.tag} {child.text}")
    dd.save()
    resourcesXml = ''
    for i in resources:
        if Misc.checkFile(i) != True:
            resourcesXml += Element.createElem("resource",i)


    output = Element.taggedElem("slot","type","user",resourcesXml)
    
    print("Generated resources")
    # return Response(status=200)
    return Response(output,status=200, mimetype='text/xml')



@app.route(f"{root}/publish",methods=["POST"])
def finalPublish():
    data = request.stream.read().decode()
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()
    ff = data.replace('<slot type="user">','<slot>')

    
    # slotFinal = LBP.genSlot("id",root.find("id").text,"1","1")
    return Response(ff,status=200, mimetype='text/xml')

@app.route(f"{root}/s/user/<typex>",methods=["GET"])
def getSlotsid(typex):
    r =  Slotsx.genSlot("id",typex,10,10)
    return Response(r,status=200, mimetype='text/xml')

@app.route(f"{root}/slots/<type>",methods=["GET"])
def getSlots(type):
    cookie = request.cookies.get("MM_AUTH")
    filter = request.args.get("gameFilterType")
    pageStart = request.args.get("pageStart")
    pageSize = request.args.get("pageSize")
    by = request.args.get("u")
    typeSlot = ''
    S = Slotsx
    match type:
        case "by":
            typeSlot = S.genSlot("user",by,pageSize,pageStart)
        case "random":
            typeSlot = S.genSlot("random",by,pageSize,pageStart)



    return Response(typeSlot,status=200, mimetype='text/xml')
    # slots = (Slots
    # .select(Slots)
    # .where(Slots.username==by)
    # .limit(pageSize)
    # .offset(pageStart)
    # )

    # slotsXml =''
    # final = ''
    # count = 0
    # for r in slots:
    #     count +=1
    #     l =Element.createElem("x",r.locationX)\
    #             +Element.createElem("y",r.locationY)\

        
    #     location = Element.createElem("location",l)
    #     rez = ''
    #     res = str(r.resource).split(";")
    #     for i in res:
    #         rez += Element.createElem("resource",i)

    #     linkss = ''
    #     link = str(r.links).split(";")
    #     for i in link:
    #         linkss += Element.createElem("id",i)
        
    #     finalLinks = Element.taggedElem("slot","type","user",linkss)



    #     # +Element.createElem("links",r[14])
        
    #     slotsXml=Element.createElem("id",r.id)\
    #             +Element.createElem("npHandle",r.username)\
    #             +Element.createElem("name",r.name)\
    #             +Element.createElem("description",r.description)\
    #             +Element.createElem("icon",r.icon)\
    #             +Element.createElem("rootLevel",r.rootLevel)\
    #             +rez\
    #             +location\
    #             +Element.createElem("initiallyLocked",r.initiallyLocked)\
    #             +Element.createElem("isSubLevel",r.isSubLevel)\
    #             +Element.createElem("isLBP1Only",r.isLBP1Only)\
    #             +Element.createElem("shareable",r.shareable)\
    #             +Element.createElem("authorLabels",r.authorLabels)\
    #             +Element.createElem("labels",r.labels)\
    #             +finalLinks\
    #             +Element.createElem("internalLinks",r.internalLinks)\
    #             +Element.createElem("leveltype",r.leveltype)\
    #             +Element.createElem("minPlayers",r.minPlayers)\
    #             +Element.createElem("maxPlayers",r.maxPlayers)\
    #             +Element.createElem("moveRequired",r.moveRequired)\
    #             +Element.createElem("heartCount",r.heartCount)\
    #             +Element.createElem("thumbsup",r.thumbsup)\
    #             +Element.createElem("thumbsdown",r.thumbdown)\
    #             +Element.createElem("averageRating",r.averageRating)\
    #             +Element.createElem("playerCount",r.playerCount)\
    #             +Element.createElem("matchingPlayers",r.matchingPlayers)\
    #             +Element.createElem("mmpick",r.mmpick)\
    #             +Element.createElem("isAdventurePlanet",r.isAdventurePlanet)\
    #             +Element.createElem("playCount",r.playCount)\
    #             +Element.createElem("completionCount",r.completionCount)\
    #             +Element.createElem("lbp1PlayCount",r.lbp1PlayCount)\
    #             +Element.createElem("lbp1CompletionCount",r.lbp1CompletionCount)\
    #             +Element.createElem("lbp1UniquePlayCount",r.lbp1UniquePlayCount)\
    #             +Element.createElem("lbp2PlayCount",r.lbp2PlayCount)\
    #             +Element.createElem("lbp2CompletionCount",r.lbp2CompletionCount)\
    #             +Element.createElem("uniquePlayCount",r.uniquePlayCount)\
    #             +Element.createElem("lbp3PlayCount",r.lbp3PlayCount)\
    #             +Element.createElem("lbp3CompletionCount",r.lbp3CompletionCount)\
    #             +Element.createElem("lbp3UniquePlayCount",r.lbp3UniquePlayCount)\
    #             +Element.createElem("reviewsEnabled",r.reviewsEnabled)\
    #             +Element.createElem("commentsEnabled",r.commentsEnabled)\
    #             +Element.createElem("publishedIn",r.publishedIn)\
    #             +Element.createElem("firstPublished",r.firstPublished)\
    #             +Element.createElem("lastUpdated",r.lastUpdated)\
    #             +Element.createElem("authorPhotoCount",r.authorPhotoCount)\
    #             +Element.createElem("photoCount",r.photoCount)\
    #             +Element.createElem("yourlbp1PlayCount",r.yourlbp1PlayCount)\
    #             +Element.createElem("yourlbp2PlayCount",r.yourlbp2PlayCount)\

    #     final += Element.taggedElem("slot","type","user",slotsXml)       
    

    # dd = Element.taggedElem2("slots","total","hint_start",str(count),count,final)

    # return Response(dd,status=200, mimetype='text/xml')
