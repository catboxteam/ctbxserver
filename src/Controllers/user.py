from peewee import *

db = SqliteDatabase("catbox.db")

class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'users'

class Users(BaseModel):
    id = PrimaryKeyField(unique=True)
    username = TextField(unique=True)
    biography = TextField(null=True)
    planetHash = TextField(null=True)
    freeSlotsLBP1 = IntegerField(null=True)
    freeSlotsLBP2 = IntegerField(null=True,default=50)
    freeSlotsLBP3 = IntegerField(null=True,default=50)
    locationX = IntegerField(null=True,default=0)
    locationY = IntegerField(null=True,default=0)
    commentsEnabled = BooleanField(default=True)
    commentsCount = IntegerField(default=0)
    heartedAuthors = IntegerField(default=0)
    heartedSlots = IntegerField(default=0)
    booHash = TextField(null=True)
    yayHash = TextField(null=True)
    photoCount = IntegerField(default="0")
    authCookie = TextField(null=True)
