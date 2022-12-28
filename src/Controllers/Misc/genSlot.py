from Controllers.Database.Slot import Slots,HeartedSlots
from Controllers.Database.Comment import Comments
from Controllers.Database.Review import Reviews
from Controllers.Database.Photo import UserPhoto
from Controllers.Elements.xml import Element
from Controllers.Misc.misc import Misc
from peewee import fn,JOIN
class Slotsx:
    def genSlot(typex,name,pageSize,pageStart):
        
        query_map = {
            "user": lambda: Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.playerId==Misc.playerToId(name)).limit(pageSize).offset(pageStart),
            "id": lambda: Slots.select(Slots).order_by(Slots.id.desc()).where(Slots.id==int(name)),
            "mmpick": lambda: Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.mmpick==True).limit(pageSize).offset(pageStart),
            "random": lambda: Slots.select(Slots).order_by(fn.Random()).limit(pageSize).offset(pageStart),
            "search": lambda: Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.name.contains(name)).limit(pageSize).offset(pageStart),
            "date": lambda: Slots.select(Slots).order_by(Slots.publishedIn.desc()).where(Slots.firstPublished>=name).limit(pageSize).offset(pageStart),
            "hearted": lambda: Slots.select(Slots).order_by(Slots.heartCount.desc()).limit(pageSize).offset(pageStart),
        }
        slots = query_map.get(typex, lambda: Slots.select(Slots))()

        final = ''
        count = 0
        for r in slots:
            count +=1
            l = Element.createElem("x", r.locationX) + Element.createElem("y", r.locationY)
            location = Element.createElem("location", l)


            res = r.resource.split(";")
            resource = ''.join(Element.createElem("resource",i) for i in res)

            link = str(r.links).split(";")
            linkss = ''.join(Element.createElem("id", i) for i in link)

            
            finalLinks = Element.taggedElem("slot","type","user",linkss)

            heartC = len(HeartedSlots.select(HeartedSlots.slotId).where(HeartedSlots.slotId==r.id))
            comments = len(Comments.select(Comments).where(Comments.toUser==name))

            reviewC = len(Reviews.select(Reviews.slotId).where(Reviews.slotId==r.id))
            photoC = len(UserPhoto.select(UserPhoto.slotId).where(UserPhoto.slotId==r.id))
            # yourReviewC = len(Reviews.select(Reviews.slotId).where(Reviews.slotId==r.id).where())

            # +Element.createElem("links",r[14])
            
            slotsXml=Element.createElem("id",r.id)\
                    +Element.createElem("npHandle",Misc.idToPlayer(r.playerId))\
                    +Element.createElem("name",r.name)\
                    +Element.createElem("description",r.description)\
                    +Element.createElem("icon",r.icon)\
                    +Element.createElem("rootLevel",r.rootLevel)\
                    +resource\
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
                    +Element.createElem("heartCount",heartC)\
                    +Element.createElem("thumbsup",r.thumbsup)\
                    +Element.createElem("thumbsdown",r.thumbdown)\
                    +Element.createElem("averageRating",r.averageRating)\
                    +Element.createElem("playerCount",r.playerCount)\
                    +Element.createElem("matchingPlayers",r.matchingPlayers)\
                    +Element.createElem("mmpick",str(r.mmpick).lower())\
                    +Element.createElem("isAdventurePlanet",r.isAdventurePlanet)\
                    +Element.createElem("playCount",r.playCount)\
                    +Element.createElem("completionCount",r.completionCount)\
                    +Element.createElem("lbp1PlayCount",r.lbp1PlayCount)\
                    +Element.createElem("lbp1CompletionCount",r.lbp1CompletionCount)\
                    +Element.createElem("lbp1UniquePlayCount",r.lbp1UniquePlayCount)\
                    +Element.createElem("lbp2PlayCount",r.lbp2PlayCount)\
                    +Element.createElem("lbp2CompletionCount",r.lbp2CompletionCount)\
                    +Element.createElem("lbp2uniquePlayCount",r.uniquePlayCount)\
                    +Element.createElem("lbp3PlayCount",r.lbp3PlayCount)\
                    +Element.createElem("lbp3CompletionCount",r.lbp3CompletionCount)\
                    +Element.createElem("lbp3UniquePlayCount",r.lbp3UniquePlayCount)\
                    +Element.createElem("reviewsEnabled","true")\
                    +Element.createElem("reviewCount",reviewC)\
                    +Element.createElem("yourReview","0")\
                    +Element.createElem("commentsEnabled",r.commentsEnabled)\
                    +Element.createElem("publishedIn",r.publishedIn)\
                    +Element.createElem("firstPublished",r.firstPublished)\
                    +Element.createElem("lastUpdated",r.lastUpdated)\
                    +Element.createElem("authorPhotoCount",r.authorPhotoCount)\
                    +Element.createElem("photoCount",photoC)\
                    +Element.createElem("commentCount",comments)\
                    +Element.createElem("yourlbp1PlayCount","0")\
                    +Element.createElem("yourlbp2PlayCount","0")\

            final += Element.taggedElem("slot","type","user",slotsXml)       
        
        # if check == "heart":
        #     dd = Element.taggedElem2("favouriteSlots","total","hint_start",str(count),count,final)
        # else:

        #     dd = Element.taggedElem2("slots","total","hint_start",str(count),count,final)
        return final