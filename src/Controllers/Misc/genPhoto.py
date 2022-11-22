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
        for i in p:
            cf = Element.createElem("id",i.slotId)
            slotType = Element.taggedElem("slot","type","developer",cf)

            photos = Element.createElem("id",i.id)\
                    +Element.createElem("author",i.username)\
                    +Element.createElem("small",i.smallHash)\
                    +Element.createElem("medium",i.mediumHash)\
                    +Element.createElem("large",i.largeHash)\
                    +Element.createElem("plan",i.planHash)\
                    +slotType\

            final += Element.taggedElem("photo","timestamp",i.timestamp,photos)
        
        return final