from peewee import *
from Controllers.Database.Connect import db
# db = SqliteDatabase("catbox.db")

class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'users'


class heartedUser(Model):
    id = PrimaryKeyField(unique=True)
    playerId = IntegerField(default=0)

    # username = TextField()
    # yayHash = TextField(null=True)
    whoHearted = TextField()
    class Meta:
        database = db
        db_table = 'favusers'

class Users(BaseModel):
    id = PrimaryKeyField(unique=True)
    username = TextField(unique=True)
    iconHash = TextField(null=True)
    biography = CharField(null=True)
    heartCount = IntegerField(null=True,default=0)
    planetHash = TextField(null=True)
    pins = TextField(null=True)
    locationX = IntegerField(null=True,default=0)
    locationY = IntegerField(null=True,default=0)
    commentsEnabled = BooleanField(default=True)
    booHash = TextField(null=True)
    yayHash = TextField(null=True)
    mehHash = TextField(null=True)
    authCookie = TextField(null=True)
