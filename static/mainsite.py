# this_file = "venv/bin/activate_this.py"
# exec(open(this_file).read(), {'__file__': this_file})
from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    application.run(debug=True)