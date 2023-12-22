
from flask_mongoengine  import MongoEngine
from flask_mongoengine import MongoEngine

url="mongodb+srv://sam:1234@cluster0.eemjyoy.mongodb.net/Bike?retryWrites=true&w=majority"



#mongodb+srv://<username>:<password>@cluster0.eemjyoy.mongodb.net/?retryWrites=true&w=majority
mydb=MongoEngine()
class Details(mydb.Document):
    bikemodel=mydb.StringField()
    bikename=mydb.StringField()
    regno=mydb.StringField()
    cc=mydb.IntField()
    stock=mydb.IntField()
    price=mydb.IntField()
    type=mydb.StringField()



