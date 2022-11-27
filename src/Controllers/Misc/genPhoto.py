from Controllers.Elements.xml import Element
from Controllers.Database.Photo import UserPhoto
# from Controllers.Database.Slot import Slots,HeartedSlots
from datetime import timedelta, date
from peewee import fn
class Photo:
    def genPhoto(ids):
        p = (UserPhoto
            .select()
            .where(UserPhoto.id==ids))
        photos = ''
        final = ''
        global slotType
        for i in p:
            cf = Element.createElem("id",i.slotId)
            d = cf+Element.createElem("name",i.name)\
                +Element.createElem("description","test")
            photos += Element.createElem("id",i.id)
            photos += Element.createElem("author",i.username)
            photos += Element.createElem("small",i.smallHash)
            photos += Element.createElem("medium",i.mediumHash)
            photos += Element.createElem("large",i.largeHash)
            photos += Element.createElem("plan",i.planHash)
            if i.subjects != "<subjects></subjects>":
                photos += i.subjects

            if i.slotId > 0:
                slotType = Element.taggedElem("slot","type","user",d)
            else:
                slotType = Element.taggedElem("slot","type","developer",d)
                # slotType = Element.taggedElem("slot","type","user",cf)
            photos += slotType


            # photos = Element.createElem("id",i.id)\
            #         +Element.createElem("author",i.username)\
            #         +Element.createElem("small",i.smallHash)\
            #         +Element.createElem("medium",i.mediumHash)\
            #         +Element.createElem("large",i.largeHash)\
            #         +Element.createElem("plan",i.planHash)\
            #         +slotType\
            #         +i.subjects

            final += Element.taggedElem("photo","timestamp",i.timestamp*1000,photos)
        
        return final