from peewee import *
from Controllers.Database.Connect import db


class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'score'


class Scores(BaseModel):
    id = PrimaryKeyField(unique=True)
    slotId = IntegerField(null=True,default=0)
    players = TextField(unique=False)
    score = IntegerField(null=True,default=0)
    rank = IntegerField(null=True,default=0)
    typeScore = IntegerField(null=True,default=0)
    isHost = BooleanField(default=False)

