from Controllers.Database.User import *
from Controllers.Database.Comment import *
from Controllers.Database.Slot import *
from Controllers.Database.Photo import *

db.create_tables([Users,Comments,UserPhoto,heartedUser,HeartedSlots,Slots])
# Users.create(username='admin')