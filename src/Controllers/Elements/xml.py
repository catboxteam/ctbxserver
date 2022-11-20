class Element:
    def createElem(name,key):
        e=f"<{name}>{key}</{name}>"
        return e
    def taggedElem(name,prename,prekey,key):
        e=f'<{name} {prename}="{prekey}">{key}</{name}>'
        return e

    def taggedElem2(name,prename,preprename,prekey,preprekey,key):
        e=f'<{name} {prename}="{prekey}" {preprename}="{preprekey}">{key}</{name}>'
        return e
