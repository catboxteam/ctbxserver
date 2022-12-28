from Controllers.Database.User import *
from Controllers.Database.Comment import *
from Controllers.Database.Slot import *
from Controllers.Database.Photo import *
from Controllers.Database.Score import *
from Controllers.Database.Queue import *
from Controllers.Database.Review import *



db.create_tables([Users,Comments,UserPhoto,heartedUser,HeartedSlots,Slots,Scores,Queue,Reviews])
# Users.create(username="Seconder45")
# Users.create(username="TestProfile",biography="For testing")