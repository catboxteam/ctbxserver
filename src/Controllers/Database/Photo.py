from peewee import *
from Controllers.Database.Connect import db


class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'photos'


class UserPhoto(BaseModel):
    id = PrimaryKeyField(unique=True)
    username = TextField(unique=False)
    timestamp = IntegerField(default=0)
    subjects = TextField(null=True,unique=False)
    smallHash = TextField(unique=False)
    mediumHash = TextField(unique=False)
    largeHash = TextField(unique=False)
    planHash = TextField(unique=False)
    slotId = IntegerField(null=True,default=0)
    rootLevel = TextField(unique=False)
    name = TextField(null=True,unique=False)

