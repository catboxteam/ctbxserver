from Controllers.Misc.misc import Misc

from flask import request,Response
from  Controllers.Misc.Files import LBPFile,fileType
from __main__ import app
import imghdr
import io
@app.route(f"{Misc.root}/upload/<sha1>",methods=["POST"])
def Upload(sha1):
    try:
        fileUpload = request.data
        file = LBPFile(fileUpload)
        isSafe = file.safeFile()
        print(f"{sha1} (Type: {file.fileType} isSafe: {isSafe})")

        if isSafe:
            # if file.fileType == fileType.Jpeg:
            #     open(f"png/{sha1}.jpeg","wb").write(fileUpload)
            # else:
            open(f"r/{sha1}","wb").write(fileUpload)
                
        else:
            return Response(status=404)


        if file.fileType == fileType.Texture:
            file.decompressFile(sha1)
        # elif file.fileType == fileType.Jpeg:


        return Response(status=200)
    except Exception as e:
        print(f"UPLOAD.PY {e}")
        # print(request.data)
        return Response(status=404)


@app.route(f"{Misc.root}/r/<sha1>",methods=["GET"])
def Read(sha1):
    try:
        return Response(response=open(f"r/{sha1}",'rb').read(),status=200)
    except Exception as e:
        print(e)
        return Response(status=404)
        
@app.route(f"{Misc.root}/showModerated",methods=["POST"])
def showModerated():
    return Response("</resources>",status=200)