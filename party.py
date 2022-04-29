"""Flask site for Balloonicorn's Party."""


from flask import Flask, session, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import Game, connect_to_db

app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


@app.route("/rsvp", methods=['POST'])
def rsvp():
    """Register for the party."""

    name = request.form.get("name")
    email = request.form.get("email")

    session['RSVP'] = True
    flash("Yay!")
    return redirect("/")


@app.route("/games")
def games():
    games = Game.query.all()

    # check if session[RSVP] exists
    # if session['RSVP']: KEYERROR!!!!!!
    if 'RSVP' in session:  # === false
        return render_template("games.html", games=games)
    else:
        return redirect('/')
    # if not, redirect to main page

    # return render_template("games.html", games=games)


if __name__ == "__main__":
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run()
