from Controllers.Database.User import Users


f = Users.select(username="Seconder45")
f.freeSlotsLBP3 = 50
f.freeSlotsLBP2 = 50
f.save()