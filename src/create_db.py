from Controllers.Database.User import *
from Controllers.Database.Comment import *
from Controllers.Database.Slot import *
from Controllers.Database.Photo import *
from Controllers.Database.Score import *
from Controllers.Database.Queue import *
from Controllers.Database.Review import *



db.create_tables([Users,Comments,UserPhoto,heartedUser,HeartedSlots,Slots,Scores,Queue,Reviews])
# for i in range(1,200):
#     Users.create(username=f'admi1ni{i}')