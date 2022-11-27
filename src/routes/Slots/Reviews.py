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


@app.route(f"{root}/reviewsFor/user/<slotid>",methods=["GET"])
def rev(slotid):
    print("test")
    return Response('<reviews></reviews>',status=200, mimetype='text/xml') 