from peewee import *
from Controllers.Database.Connect import db

class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'queue'


class Queue(BaseModel):
    id = PrimaryKeyField(unique=True)
    slotId = IntegerField(null=True,default=0)
    # player = TextField(unique=False)
    playerId = IntegerField(default=0)
