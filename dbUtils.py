from flask_sqlalchemy import SQLAlchemy
import hashlib

# Here I define a really simple database
# database are mainly like excel files so you have to define
# for each sheet what are the column name.
# And then, you'll create new entry inside, as shown in the app.py file for the envoicontact function 


db = SQLAlchemy()




class newsletter(db.Model):
    __tablename__ = 'newsletter'
    name=db.Column(db.String(100))
    mail = db.Column(db.String(100),primary_key=True)

    def __init__(self,name,mail):
        self.name=name
        self.mail=mail
        
