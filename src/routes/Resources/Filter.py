from Controllers.Misc.misc import Misc

from flask import request,Response
from __main__ import app
@app.route(f"{Misc.root}/filter",methods=["POST"])
def filters():
    return request.data.decode()