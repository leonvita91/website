

from flask import * 
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView




#Init the Web
app = Flask (__name__)








@app.route("/")
def home():
    return render_template("home.html")

#partner
@app.route("/associate")
def team():
    return render_template("associate.html")


#About_us
@app.route("/about_us")
def about():
    return render_template("about_us.html")
    #return "This is about us"







#End Init the Web
if __name__ == "__main__":
    app.run(debug=True)
