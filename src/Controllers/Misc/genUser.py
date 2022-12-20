from Controllers.Database.Slot import HeartedSlots,Slots
from Controllers.Database.User import Users,heartedUser
from Controllers.Database.Comment import Comments
from Controllers.Database.Photo import UserPhoto
from Controllers.Database.Queue import Queue
from Controllers.Elements.xml import Element



class GeneratedUser:
    def genUsr(name):
        user = Users.get(username=name)
        

        slots = len(Slots
        .select()
        .where(Slots.publishedIn=="lbp2")
        .where(Slots.username==name))

        allslots = len(Slots
        .select()
        .where(Slots.username==name))

        comments = len(Comments
        .select(Comments)
        .where(Comments.toUser==name))

        favSlots = len(HeartedSlots
            .select(HeartedSlots)
            .where(HeartedSlots.username==name))

        userCount = len(heartedUser
            .select(heartedUser.whoHearted)
            .where(heartedUser.whoHearted==name))

        heartCount = len(heartedUser
            .select(heartedUser.username)
            .where(heartedUser.username==name))

        photosCount = len(UserPhoto
            .select(UserPhoto.username)
            .where(UserPhoto.username==name))

        photoWithMeCount = len(UserPhoto
            .select(UserPhoto.username)
            .where(UserPhoto.username!=name)
            .where(UserPhoto.subjects.contains(name)))
            
        queueCount = len(Queue
            .select(Queue.player)
            .where(Queue.player==name))
        
        location = Element.createElem("x",user.locationX) + Element.createElem("y",user.locationY)
        finalResult = Element.createElem("location",location)

        final = Element.taggedElem("npHandle","icon",user.iconHash,user.username)
        final += Element.createElem("game","2")
        final += Element.createElem("lbp1UsedSlots","0")
        final += Element.createElem("entitledSlots","50")
        final += Element.createElem("freeSlots",50-allslots)

        final += Element.createElem("crossControlUsedSlots","0")
        final += Element.createElem("crossControlEntitledSlots","50")
        final += Element.createElem("crossControlPurchasedSlots","0")
        final += Element.createElem("crossControlFreeSlots","50")

        final += Element.createElem("lbp2UsedSlots",slots)
        final += Element.createElem("lbp2EntitledSlots","50")
        final += Element.createElem("lbp2PurchasedSlots","0")
        final += Element.createElem("lbp2FreeSlots",50-slots)

        final += Element.createElem("lbp3UsedSlots","0")
        final += Element.createElem("lbp3EntitledSlots","50")
        final += Element.createElem("lbp3PurchasedSlots","0")
        final += Element.createElem("lbp3FreeSlots","50")

        final += Element.createElem("lists_quota","50")
        final += Element.createElem("heartCount",heartCount)
        final += Element.createElem("planets",user.planetHash)
        final += Element.createElem("crossControlPlanet",user.planetHash)
        final += Element.createElem("yay2",user.yayHash)
        final += Element.createElem("boo2",user.booHash)
        final += Element.createElem("meh2",user.booHash)
        final += Element.createElem("biography",user.biography)
        final += Element.createElem("reviewCount",user.reviewCount)
        final += Element.createElem("commentCount",comments)

        final += Element.createElem("photosByMeCount",photosCount)
        final += Element.createElem("photosWithMeCount",photoWithMeCount)

        final += Element.createElem("commentsEnabled",user.commentsEnabled)
        final += finalResult
        final += Element.createElem("favouriteSlotCount",favSlots)
        final += Element.createElem("favouriteUserCount",userCount)
        final += Element.createElem("lolcatftwCount",queueCount)


        final += Element.createElem("pins",user.pins)

        finalUser = Element.taggedElem("user","type","user",final)

        return finalUser