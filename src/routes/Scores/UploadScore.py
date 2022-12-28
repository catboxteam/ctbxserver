from Controllers.Misc.misc import Misc


from Controllers.Database.Score import *
from Controllers.Elements.xml import Element
from flask import request,Response
from Controllers.Misc.misc import *
import xml.etree.ElementTree as ET
from __main__ import app
import io

#/topscores/user/6/1?pageStart=1&pageSize=5
#/scoreboard/user/6?lbp2=true

def test(id):
    q = (Scores.select()
            .where(Scores.id==id)
            .order_by(Scores.score.desc()))
    d = 0
    final = ''
    f = ''
    for i in q:
        d += 1
        f += Element.createElem("mainPlayer",i.players)
        f += Element.createElem("score",i.score)
        f += Element.createElem("rank",d)

        final += Element.createElem("playRecord",f)

    return final



@app.route(f"{Misc.root}/topscores/user/<slotId>/<players>",methods=["GET"])
def getScore(slotId,players):

    # t = test(slotId)

    get = (Scores.select()
      .where(Scores.slotId==slotId))

    g = ''
    count = 0
    for i in get:
      count+=1
      g+= test(i.id)

  
    dd = Element.taggedElem("scores","totalNumScores",count,g)

    return Response(dd,status=200, mimetype='text/xml')


@app.route(f"{Misc.root}/scoreboard/user/<slotId>",methods=["POST"])
def uploadScore(slotId):
    data = request.stream.read().decode()
    cookie = request.cookies.get("MM_AUTH")
    f = io.StringIO(data)
    tree = ET.parse(f)
    root = tree.getroot()

    sc = Scores(slotId=slotId)

    for child in root:
        match child.tag:
            case "host":
              sc.isHost = child.text
            case "type":
              sc.typeScore = child.text
            case "playerIds":
              sc.players = child.text
            case "score":
              sc.score = child.text

    sc.save()

    print(request.data.decode())
    # return Response(fff,status=200, mimetype='text/xml')
    # <playRecord>
    # <host>true</host>
    # <type>1</type>
    # <playerIds>Seconder45</playerIds>
    # <score>1800</score>
    # </playRecord>
