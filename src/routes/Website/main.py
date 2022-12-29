from Controllers.Misc.misc import Misc

from flask import request,render_template,url_for,send_file
from __main__ import app
from Controllers.Database.User import Users
from Controllers.Database.Slot import Slots
import io

@app.route("/")
def index():
    slotss = Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.mmpick==True).limit(4)
    new = Slots.select(Slots).order_by(Slots.publishedIn.desc()).limit(4)

    return render_template('index.html',slots=slotss,newSlots=new)

@app.route("/users/<int:page>")
def usr(page):
    usr = Users.select()
    pageint = usr.paginate(page,5)
    count = len(pageint)
    
    return render_template('users.html',data=pageint,page=page,usrcount=count)

@app.route("/levels")
def level():
    slotss = Slots.select()
    return render_template('levels.html',slots=slotss)

@app.route("/photos")
def photo():
    return render_template('photos.html')


@app.route("/image/<sha1>")
def imageGet(sha1):
    try:
        return send_file(io.BytesIO(open(f"png/{sha1}.png","rb").read()),mimetype='image/png')
    except FileNotFoundError:
        return send_file(io.BytesIO(open(f"png/62c51cd8a06c1a98fe4d6ef4739951dd6eeda359.png","rb").read()),mimetype='image/png')
