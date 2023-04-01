
Here's the Readme for this website


I've not said that for the moment, but you'll have to do some stuff before beginning:
install python on you re pc (the programming language), pip (something to manage python extensions)
VSCode (an helpfull text editor specialized for code), and then you'll have to install different usefull 
python extensions for our purpose : 
Flask (this one is used to create the different routes, you need it as it's the root of all we're gonna make)
Flask-Mail (if you want you re website to send mail, for a contact us page for exemple)
Flask-SQLAlchemy (if you want to deal with a data base)

Theses things are called the environnement you re working in (that's just the name)

Main code is written in the app.py (The first two commented lines are only usefull for the hosting)

Every .py files are made to perform some computation, when you go on the website, that's the app.py file that is trigger and then it
will do it's stuff and render the page

(You have to be carefull with static and templates folder, because you have to name yours the same as the language we use is looking for them)
In the templates folder you'll file tons of .html files
theses html files are made to create the display thanks to html programming language (This is what I mainly steal from other websites lol).
You could find some greate exemples on web by searching 'html css (what you want to do) exemple'.

https://alvarotrigo.com/blog/html-css-timelines/
For exemple, here s the first website I found by looking for html css timeline

Then in static : 
You'll put every resources you're website needs : the pictures, the songs if there is, ALL.
You'll find a subfolder css and another one js in mine, I recommand you to do the same, and to get everything
tidy, because each change in the filesystem structure will result in changes in the code (we don't want that of course)

The CSS thing:
css is another language make to custom html, it's usefull to change it's default parameters, and to allow things to look as you want them to look.
Be carefull when stealing it from other website, sometimes it's writtend scss, that's another version, so you'll have to use an online converter to get it works with css (very easy, but if you don't know that that's boring Lol)
->You can specifie some things for special screen sizes (for exemple for mobile phone or desktop pc), it's very powerfull,
and if you steal code, the one that written the code has probably already did that

The JS thing : 
This one is for the responsive stuff, moving stuff and else. For real, just steal it if you need, but for the moment, I know how this works but I've never developped anything with it, only stealing (and this little game)

The other folders are just used to put the images inside.

All right so quick summary :
html/css : display/something to make the display prettier
js : make it move
pythin file : the backend of our website, that do all the computation


For the html things, I'll only comment the base and the contact ones as it's almost the same everytime,
and once you understood there's no point of doing more ^^.

For the css, I'll comment flip.css as this is one of those I know the most !