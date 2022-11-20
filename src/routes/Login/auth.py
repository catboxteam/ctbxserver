from flask import request,Response
from __main__ import app
from Controllers.Tickets import genAuth,parseTicket

root = "/LITTLEBIGPLANETPS3_XML"
@app.route(f'{root}/login',methods=['POST'])
def login():
    ticket = parseTicket.parseTicket(request.data)
    ap = genAuth.Ticket()
    auth = ap.genAuth(ticket.username)
    print(auth)
    return Response(auth,status=200, mimetype='text/xml')