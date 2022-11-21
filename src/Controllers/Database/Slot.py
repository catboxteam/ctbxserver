from peewee import *
from Controllers.Database.Connect import db
# db = SqliteDatabase("catbox.db")

class BaseModel(Model):
    class Meta:
        database = db
        db_table = 'slots'


class HeartedSlots(Model):
    id = PrimaryKeyField(unique=True)
    username = TextField()
    slotId = IntegerField(null=True,default=0)
    class Meta:
        database = db
        db_table = "favslots"

class Slots(BaseModel):
    id = PrimaryKeyField(unique=True)
    username = TextField()
    name = TextField(null=True)
    icon = TextField(null=True)
    description = TextField(null=True)
    iconLevel = TextField(null=True)
    rootLevel = TextField(null=True)
    resource = TextField(null=True)
    locationX = IntegerField(null=True,default=0)
    locationY = IntegerField(null=True,default=0)
    initiallyLocked = BooleanField(null=True,default=False)
    isSubLevel = BooleanField(null=True,default=False)
    isLBP1Only = BooleanField(null=True,default=False)
    shareable = TextField(null=True)
    authorLabels = TextField(null=True)
    links = TextField(null=True)
    internalLinks = TextField(null=True)
    leveltype = TextField(null=True)
    background = TextField(null=True)
    minPlayers = IntegerField(null=True,default=0)
    maxPlayers = IntegerField(null=True,default=0)
    moveRequired = BooleanField(null=True,default=False)
    labels = TextField(null=True)



    heartCount = IntegerField(default=0)
    thumbsup = IntegerField(default=0)
    thumbdown = IntegerField(default=0)
    averageRating = IntegerField(default=0)
    playerCount = IntegerField(default=0)
    matchingPlayers = IntegerField(default=0)
    mmpick = BooleanField(default=False)
    playCount = IntegerField(default=0)
    completionCount = IntegerField(default=0)

    lbp1PlayCount = IntegerField(default=0)
    lbp1CompletionCount = IntegerField(default=0)
    lbp1UniquePlayCount = IntegerField(default=0)

    lbp2PlayCount = IntegerField(default=0)
    lbp2CompletionCount = IntegerField(default=0)
    lbp2UniquePlayCount = IntegerField(default=0)

    lbp3PlayCount = IntegerField(default=0)
    lbp3CompletionCount = IntegerField(default=0)
    lbp3UniquePlayCount = IntegerField(default=0)

    reviewsEnabled = BooleanField(default=False)
    commentsEnabled = BooleanField(default=False)

    publishedIn = IntegerField(default="lbp2")




    uniquePlayCount = IntegerField(default=0)





    firstPublished = IntegerField(default=0)
    lastUpdated = IntegerField(default=0)
    commentEnabled = BooleanField(default=False)
    isAdventurePlanet = BooleanField(default=False)
    authorPhotoCount = IntegerField(default=0)
    photoCount = IntegerField(default=0)
    












