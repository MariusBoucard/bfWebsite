this_file = "venv/bin/activate_this.py"
exec(open(this_file).read(), {'__file__': this_file})

# First of all you needs to import everything you'll need
import smtplib
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
# theses are some things written in another file called dbUtils
#BTW, you should create an empty __init__.py file as I did to allow you this kind of stuff
#It s a good practice to split code into differents files
from dbUtils import newsletter
import os
import folder as f
import xmlutils
from flask_sslify import SSLify

# Create the application
application = Flask(__name__)
# Some secrets things
application.secret_key = 'BFSecret'
#NAME OF OUR DATABASE ON THE RIGHT
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BFekal.sqlite3'
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(application)

##############
#MAIL SERVER CONFIG, YOU'LL HAVE TO PUT YOU RE OWN CREDITENTIALS, DEPENDS ON YOUR PROVIDER

sslify = SSLify(application)
application.config['MAIL_SERVER'] = 'smtp.laposte.net'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USERNAME'] = 'brutalfekal@laposte.net'
application.config['MAIL_PASSWORD'] = 'BFForever4435!'
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_DEFAULT_SENDER'] = 'brutalfekal@laposte.net'
mail = Mail(application)
mail = Mail(application)    

# This is a route, you'll use it to render any of you pages
# so when you go to the homepage of the website (with / after the domain name, it triggers this function)
# And then this function will only render the index.html file (it will search for it into the template folder, 
# if it s in a template subfolder you'll have to explain the path like this : subfoldername/index.html)
@application.route("/")
def index():
    return render_template("index.html")

# Again the same kind of stuff, when you'll go to brutalfekal.com/brutalfekallegend, it will display this page
@application.route("/brutalfekallegend")
def story():
    return render_template("story2.html")

@application.route("/brutalnews")
def news():
    return render_template("news.html")    

@application.route("/brutalfekallegend2")
def story2():
    return render_template("story.html")

@application.route("/nouschieralaraie")
def contact():
    return render_template("contact.html")

@application.route("/brutalpub")
def newslet():
    return render_template("Newsletter.html")

@application.route("/nocookies")
def nocookies():
    return render_template("nocookies.html")

# This one is quite different, there's some computation in it because I use data.
# The website user will send us some data, so we have to specify methods=["GET","POST"]
#POST is used to let user send us data and get is used to let him get some data from us,
# all the previous routes use get
@application.route("/newsinscription",methods=["GET","POST"])
def newsinsc():
    # I check if user did a POST request
     if request.method=="POST":
        # try:
        #    Then I take the creditentials he putted in the form (you'll find this form in Newsletter.html)
        # In this form I defined some keys that are used here to get the data user put into the website
            name = request.form['name']
            mailusr =request.form['mail']
            # Here's I m asking the database if it knows the user (as a newsletter object)
            exists = newsletter.query.filter_by(mail=mailusr).first()
            if not exists :
                # if not, it will create a new newsletter object and put it inside
                # newsletter is a complexe object carrying user name and it s mail
                # You'll find how I did this object in dbUtils.py file, that's why I've imported it earlier
                usr = newsletter(name,mailusr)
                db.session.add(usr)
                db.session.commit()
                flash("C'est bon t es inscrit mon brave")
            else:
                flash("Cet adresse mail est déja inscrite !")
     return redirect(url_for("newslet"))

# Here, it will be hard to explain, but mainly, I look into the picture folder for every subdirectory
# For each one of theses, I look if there is a config.xml file in it,
# If there is, I show the image written as folder cover inside this xml file
@application.route("/brutalimages")
def images():
    #First : Get all the differents directory inside :
    caca = os.walk("./static/images/brutalimages")
    folderlist = [x[1] for x in caca]
    caca = folderlist[0]
    JustTheRightFolder = []
    for folder in caca :
        if os.path.exists("./static/images/brutalimages/"+folder+"/config.xml") :
            JustTheRightFolder.append(folder)
    #Into folder dict their will be the folder path as key and then the whole created folder as value
    folderDict = {}
    for foldername in JustTheRightFolder :
       folderInfo = xmlutils.getFolderInfo("./static/images/brutalimages/"+foldername+"/config.xml")
       folderobj = f.folder(folderInfo.get('name'),folderInfo.get('description'),folderInfo.get('date'),folderInfo.get('cover'),folderInfo.get("foldernum"))
       folderDict.update({foldername : folderobj})

    dict1={}
    dict2={}
    dict3={}
    #We have to split it in 3 differents dicts
    for fold in folderDict.keys() :
        if int(folderDict.get(fold).foldernum) %3==0:
            dict1.update({fold : folderDict.get(fold)})
        if int(folderDict.get(fold).foldernum)%3==1:
            dict2.update({fold : folderDict.get(fold)})
        if int(folderDict.get(fold).foldernum) %3==2:
            dict3.update({fold : folderDict.get(fold)})
    
    # First it has to parse all the none empty folder it has in ourimages
    return render_template("folderimage.html",folderDict = folderDict,dict1=dict1,dict2=dict2,dict3=dict3)

# Same than the previous one, but for the images inside the subfolder
# btw, I use some functions written in other files that I ve imported at the beginning of the program  xmlutils.getimageList for exemple
@application.route("/brutalimagefolder/<folder>")
def bfimgfolder(folder):
    #On doit parse le xml pour récupérer toutes les images dedans
    if not os.path.exists("./static/images/brutalimages/"+folder+"/config.xml") :
        return redirect(url_for("index"))
    else :
        folderInfo = xmlutils.getFolderInfo("./static/images/brutalimages/"+folder+"/config.xml")
        folderobj = f.folder(folderInfo.get('name'),folderInfo.get('description'),folderInfo.get('date'),folderInfo.get('cover'),folderInfo.get("foldernum"))
        imagesXML = xmlutils.getimageList("./static/images/brutalimages/"+folder+"/config.xml")
        print(imagesXML[0].portrait)

    return render_template("imggallery.html",images=imagesXML,folder=folder,folderobj=folderobj)

@application.route("/artworks")
def artworks():
   return render_template("artworks.html")
@application.route("/brutalbanger")
def brutalbanger():
   return render_template("artworks.html")


@application.route("/brutalfekal")
def fekal():
   return render_template("notregroupe.html")

@application.route("/merch")
def merch():
    return render_template("merch.html")

# This part is to send an Email ! You have to take everything from the form you ve defined in the html page,
# And then, use you re email adress to send you this data by email (you might even add another send to the user)
@application.route("/sendmessage",methods=["GET","POST"])
def envoicontact():
    global mail
    if request.method=="POST":
        try:
            if request.form.get("newsletter"):
                name = request.form['name']
                mailusr =request.form['mail']
                exists = newsletter.query.filter_by(mail=mailusr).first()
                if not exists :
                    usr = newsletter(name,mailusr)
                    db.session.add(usr)
                    db.session.commit()
                else:
                    flash("Cet adresse mail est déja inscrite !")
            objet = "[CONTACT SITE] : "+request.form["objet"]
            texte = request.form["corpsmail"]
            adresse = request.form["mail"]
            msg = Message(objet, sender = application.config['MAIL_USERNAME'], recipients = ['brutalfekal4435@gmail.com'])
            msg.body =adresse+" veut vous envoyer ce message :\n"+texte
            print("nice")
            mail.send(msg)
            flash("Message bien envoyé !")
        except:
            flash("As tu bien remplis tous les champs ?")
    return redirect(url_for("contact"))

# THe redirect thing is just to prevent creating new routes, it redirects toward another one
# This part is the code that's executed when you lauch the app : 2 lines that makes everything
if __name__ == "__main__":
    db.create_all()
    application.run(debug=True,host="0.0.0.0",port="5001")