root = "/LITTLEBIGPLANETPS3_XML"
from Controllers.Elements.xml import Element
from Controllers.Misc.genPhoto import Photo
from Controllers.Database.Photo import *
from Controllers.Database.User import *
from flask import request,Response
import xml.etree.ElementTree as ET
from __main__ import app
import io

@app.route(f'{root}/uploadPhoto',methods=['POST'])
def upload():
    data = request.stream.read().decode()
    cookie = request.cookies.get("MM_AUTH")
    usr = Users.select().where(Users.authCookie == cookie).get().username
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()

    createPhoto = UserPhoto()
    createPhoto.username = usr
    # author = root.find("author").text
    smallHash = root.find("small").text
    mediumHash = root.find("medium").text
    largeHash = root.find("large").text
    planHash = root.find("large").text
    createPhoto.smallHash = smallHash
    createPhoto.mediumHash = mediumHash
    createPhoto.largeHash = largeHash
    createPhoto.planHash = planHash
    
    slot = root.find("slot")
    timestamp = root.attrib["timestamp"]
    createPhoto.timestamp = timestamp

    match slot.attrib["type"]:
        case "developer":
            print("wip")
        case "pod":
            print("ok")
            createPhoto.rootLevel = slot.find("rootLevel").text
            createPhoto.name = slot.find("name").text
        case "user":
            createPhoto.slotId = slot.find("id").text
            createPhoto.rootLevel = slot.find("rootLevel").text
            createPhoto.name = slot.find("name").text


    print(data)
    createPhoto.save()
    
    idReturn = Element.createElem("id",createPhoto.id)
    r = Element.createElem("photo",idReturn)
    return Response(response=r, status=200, mimetype="application/xml")


@app.route(f'{root}/photos/by',methods=['GET'])
def getPhotos():
    by = request.args.get('user')
    pageStart = int(request.args.get("pageStart")) -1
    pageSize = int(request.args.get("pageSize"))

    cc = (UserPhoto
        .select()
        .where(UserPhoto.username==by)
        .order_by(UserPhoto.timestamp.desc())
        .limit(pageSize)
        .offset(pageStart)
    )
    f = ''
    for i in cc:
        f += Photo.genPhoto(i.id)

    final2 = Element.createElem("photos",f)
    return Response(response=final2, status=200, mimetype="application/xml")


        
        


                

