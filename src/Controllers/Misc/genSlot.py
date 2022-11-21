from Controllers.Elements.xml import Element
from Controllers.Database.Slot import Slots
from datetime import timedelta, date
from peewee import fn
class Slotsx:
    def genSlot(typex,name,pageSize,pageStart):

        slots = ''
        if typex == "user":
            slots = (Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.username==name).limit(pageSize).offset(pageStart))
        elif typex == "id":
            slots = (Slots.select(Slots).order_by(Slots.id.desc()).where(Slots.id==int(name)))
        elif typex == "mmpick":
            slots = (Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.mmpick==name).limit(pageSize).offset(pageStart))
        elif typex == "random":
            slots = (Slots.select(Slots).order_by(fn.Random()).limit(pageSize).offset(pageStart))
        elif typex == "search":
            slots = (Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.name.contains(name)).limit(pageSize).offset(pageStart))

        slotsXml =''
        final = ''
        count = 0
        for r in slots:
            count +=1
            l =Element.createElem("x",r.locationX)\
                    +Element.createElem("y",r.locationY)\

            
            location = Element.createElem("location",l)
            rez = ''
            res = str(r.resource).split(";")
            for i in res:
                rez += Element.createElem("resource",i)

            linkss = ''
            link = str(r.links).split(";")
            for i in link:
                linkss += Element.createElem("id",i)
            
            finalLinks = Element.taggedElem("slot","type","user",linkss)



            # +Element.createElem("links",r[14])
            
            slotsXml=Element.createElem("id",r.id)\
                    +Element.createElem("npHandle",r.username)\
                    +Element.createElem("name",r.name)\
                    +Element.createElem("description",r.description)\
                    +Element.createElem("icon",r.icon)\
                    +Element.createElem("rootLevel",r.rootLevel)\
                    +rez\
                    +location\
                    +Element.createElem("initiallyLocked",r.initiallyLocked)\
                    +Element.createElem("isSubLevel",r.isSubLevel)\
                    +Element.createElem("isLBP1Only",r.isLBP1Only)\
                    +Element.createElem("shareable",r.shareable)\
                    +Element.createElem("authorLabels",r.authorLabels)\
                    +Element.createElem("labels",r.authorLabels)\
                    +finalLinks\
                    +Element.createElem("internalLinks",r.internalLinks)\
                    +Element.createElem("leveltype",r.leveltype)\
                    +Element.createElem("minPlayers",r.minPlayers)\
                    +Element.createElem("maxPlayers",r.maxPlayers)\
                    +Element.createElem("moveRequired",r.moveRequired)\
                    +Element.createElem("heartCount",r.heartCount)\
                    +Element.createElem("thumbsup",r.thumbsup)\
                    +Element.createElem("thumbsdown",r.thumbdown)\
                    +Element.createElem("averageRating",r.averageRating)\
                    +Element.createElem("playerCount",r.playerCount)\
                    +Element.createElem("matchingPlayers",r.matchingPlayers)\
                    +Element.createElem("mmpick",r.mmpick)\
                    +Element.createElem("isAdventurePlanet",r.isAdventurePlanet)\
                    +Element.createElem("playCount",r.playCount)\
                    +Element.createElem("completionCount",r.completionCount)\
                    +Element.createElem("lbp1PlayCount",r.lbp1PlayCount)\
                    +Element.createElem("lbp1CompletionCount",r.lbp1CompletionCount)\
                    +Element.createElem("lbp1UniquePlayCount",r.lbp1UniquePlayCount)\
                    +Element.createElem("lbp2PlayCount",r.lbp2PlayCount)\
                    +Element.createElem("lbp2CompletionCount",r.lbp2CompletionCount)\
                    +Element.createElem("uniquePlayCount",r.uniquePlayCount)\
                    +Element.createElem("lbp3PlayCount",r.lbp3PlayCount)\
                    +Element.createElem("lbp3CompletionCount",r.lbp3CompletionCount)\
                    +Element.createElem("lbp3UniquePlayCount",r.lbp3UniquePlayCount)\
                    +Element.createElem("reviewsEnabled",r.reviewsEnabled)\
                    +Element.createElem("commentsEnabled",r.commentsEnabled)\
                    +Element.createElem("publishedIn",r.publishedIn)\
                    +Element.createElem("firstPublished",r.firstPublished)\
                    +Element.createElem("lastUpdated",r.lastUpdated)\
                    +Element.createElem("authorPhotoCount",r.authorPhotoCount)\
                    +Element.createElem("photoCount",r.photoCount)\
                    +Element.createElem("yourlbp1PlayCount","0")\
                    +Element.createElem("yourlbp2PlayCount",r"0")\

            final += Element.taggedElem("slot","type","user",slotsXml)       
        
        # if check == "heart":
        #     dd = Element.taggedElem2("favouriteSlots","total","hint_start",str(count),count,final)
        # else:

        #     dd = Element.taggedElem2("slots","total","hint_start",str(count),count,final)
        return final