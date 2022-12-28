from Controllers.Misc.misc import Misc

from flask import request,render_template,url_for
from playhouse.flask_utils import object_list,PaginatedQuery
from __main__ import app
from Controllers.Database.User import Users
from Controllers.Database.Slot import Slots

@app.route("/")
def index():
    slotss = Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.mmpick==True).limit(4)
    new = Slots.select(Slots).order_by(Slots.publishedIn.desc()).limit(4)

    return render_template('index.html',slots=slotss,newSlots=new)

@app.route("/users/<int:page>")
def usr(page):
    usr = Users.select()
    pageint = usr.paginate(page,5)
    count = pageint.count()
    return render_template('users.html',data=pageint,page=page,usrcount=count)
    # return object_list('users.html',query=pageint,paginate_by=5)

@app.route("/levels")
def level():
    slotss = Slots.select()
    return render_template('levels.html',slots=slotss)

@app.route("/photos")
def photo():
    return render_template('photos.html')