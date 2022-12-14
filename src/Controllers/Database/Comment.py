from peewee import *
from Controllers.Database.Connect import db


# db = SqliteDatabase("catbox.db")

class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'comments'

class Comments(BaseModel):
    id = PrimaryKeyField(unique=True)
    playerId = IntegerField(default=0)
    # username = TextField(unique=False)
    message = TextField(unique=False)
    timestamp = IntegerField(default=0)
    toUser = TextField(unique=False)
    isDeleted = BooleanField(default=False)
    deletedType = TextField(null=True)
    deletedUser = TextField(null=True)
    up = IntegerField(default=0)
    down = IntegerField(default=0)
    
