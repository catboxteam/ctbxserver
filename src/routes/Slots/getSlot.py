root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Database.Comment import Comments
from Controllers.Database.Slot import Slots,HeartedSlots
from Controllers.Database.Review import Reviews
from Controllers.Database.User import Users
from Controllers.Database.Queue import Queue
from Controllers.Database.Score import Scores
from Controllers.Elements.xml import Element
from Controllers.Misc.genSlot import Slotsx
from Controllers.Misc.misc import Misc
from datetime import timedelta, date
from flask import request,Response
from Controllers.Misc.misc import *
import xml.etree.ElementTree as ET
from __main__ import app
import io


@app.route(f"{root}/startPublish",methods=["POST"])
def startPublish():
    startPub = Misc.timestamp()

    # data = request.stream.read().decode()
    data = request.data.decode()
    cookie = request.cookies.get("MM_AUTH")
    user = Users.select().where(Users.authCookie == cookie).get().username
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()

    resources = []
    links = []

    # dd,c = Slots.get_or_create(id=root.find("id").text,username=user)    
    if root.find("id") == None:
        dd = Slots(username=Users.select().where(Users.authCookie == cookie).get().username)
        dd.firstPublished = startPub
    else:
        dd = Slots.select().where(Slots.id==root.find("id").text).get()

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

    dd.lastUpdated = startPub


    if user != dd.username:
        print("waste of time")
        return Response(status=403)
    else:
        dd.save()

    resourcesXml = ''
    for i in resources:
        if Misc.checkFile(i) != True:
            resourcesXml += Element.createElem("resource",i)


    output = Element.taggedElem("slot","type","user",resourcesXml)
    
    print("Generated resources")

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

# @app.route(f"{root}/slots/",methods=["GET"])

@app.route(f"{root}/slots/lolcatftw/<user>",methods=["GET"])
def getlolcat(user):
    pageStart = int(request.args.get("pageStart"))-1
    pageSize = request.args.get("pageSize")

    getFav = (Queue.select().where(Queue.player==user))
    f =''
    for i in getFav.objects():
        f += Slotsx.genSlot("id",i.slotId,pageSize,pageStart)
    dd = Element.taggedElem2("slots","total","hint_start",122,122,f)

    return Response(response=dd, status=200, mimetype="application/xml")


@app.route(f"{root}/lolcatftw/remove/user/<id>",methods=["POST"])
def removelolcat(id):
    cookie = request.cookies.get("MM_AUTH")
    User = Users.select().where(Users.authCookie == cookie).get()

    d = Queue.delete().where(Queue.player==User.username).where(Queue.slotId==id)

    d.execute()
    return Response(status=200)




@app.route(f"{root}/slots",methods=["GET"])
def get():
    pageStart = int(request.args.get("pageStart"))-1
    pageSize = request.args.get("pageSize")
    q = (Slots.select()
            .order_by(Slots.firstPublished.desc()))
    f =''
    for i in q:
        f += Slotsx.genSlot("id",i.id,pageSize,pageStart)

    dd = Element.taggedElem2("slots","total","hint_start",122,122,f)

    return Response(response=dd, status=200, mimetype="application/xml")


@app.route(f"{root}/slots/<type>",methods=["GET"])
def getSlots(type):
    cookie = request.cookies.get("MM_AUTH")
    filter = request.args.get("gameFilterType")
    pageStart = int(request.args.get("pageStart"))-1
    pageSize = int(request.args.get("pageSize"))
    by = request.args.get("u")
    search = request.args.get("query")

    typeSlot = ''
    date1 = ''
    match type:
        case "developer":
            print("WIP")
        case "by":
            typeSlot = Slotsx.genSlot("user",by,pageSize,pageStart)
        case "lbp2luckydip":
            typeSlot = Slotsx.genSlot("random",by,pageSize,pageStart)
        case "mmpicks":
            typeSlot = Slotsx.genSlot("mmpick",by,pageSize,pageStart)
        case "search":
            typeSlot = Slotsx.genSlot("search",search,pageSize,pageStart)
        case "mostHearted":

            dateFilterType = request.args.get("dateFilterType")
            print(dateFilterType)
            if dateFilterType:
                if dateFilterType == "thisMonth":
                    date1 = date.today() + timedelta(days=-31)
                elif dateFilterType=="thisWeek":
                    date1 = date.today() + timedelta(days=-7)

                convert = time.mktime(date1.timetuple()) * 1000

                typeSlot = Slotsx.genSlot("date",int(convert),pageSize,pageStart)
            else:
                typeSlot = Slotsx.genSlot("hearted",None,pageSize,pageStart)
        case _:
            print(f"Not found")

    finalSlot = Element.taggedElem2("slots","total","hint_start",pageStart + pageSize,pageStart,typeSlot)


    return Response(finalSlot,status=200, mimetype='text/xml')


@app.route(f"{root}/unpublish/<id>",methods=["POST"])
def delSlot(id):
    ee = Slots.get_by_id(id)

    commentsDelete = Comments.delete().where(Comments.toUser==id)
    heartDelete = HeartedSlots.delete().where(HeartedSlots.slotId==id)
    queueDelete = Queue.delete().where(Queue.slotId==id)
    scoreDelete = Scores.delete().where(Scores.slotId==id)
    reviewsDelete = Reviews.delete().where(Reviews.slotId==id)


    scoreDelete.execute()
    queueDelete.execute()
    commentsDelete.execute()
    heartDelete.execute()
    reviewsDelete.execute()
    # ee = Slots.delete().where

    ee.delete_instance(recursive=True)

    return Response(status=200)
