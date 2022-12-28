from peewee import *
from Controllers.Database.Connect import db

class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'reviews'


class Reviews(BaseModel):
    id = PrimaryKeyField(unique=True)
    slotId = IntegerField(null=True,default=0)
    # username = TextField()
    playerId = IntegerField(default=0)
    timestamp = IntegerField(null=True,default=0)
    deleted = TextField(default="false")
    deletedBy = TextField(unique=False,default="none")
    text = TextField(null=True)
    labels = TextField(null=True)
    thumb = TextField(null=True)
    thumbsup = IntegerField(null=True,default=0)
    thumbsdown = IntegerField(null=True,default=0)
    


