from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap4




app = Flask(__name__)

bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")








if __name__ == "__main__":
    app.run(debug=True)