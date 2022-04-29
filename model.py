from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    Game.query.delete()

    # add some sample games
    game1 = Game(name='Tic-Tac-Toe', description='fun game of X and O')
    game2 = Game(name='Machi Koro', description='the best board game ever')
    game3 = Game(name='Tickets to Ride', description='another board game')
    game4 = Game(name='Monopoly', description='the best board game really!!!')
    db.session.add_all([game1, game2, game3, game4])
    db.session.commit()


'''
def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Employee.query.delete()
    Department.query.delete()

    # Add sample employees and departments
    df = Department(dept_code='fin', dept='Finance', phone='555-1000')
    dl = Department(dept_code='legal', dept='Legal', phone='555-2222')
    dm = Department(dept_code='mktg', dept='Marketing', phone='555-9999')

    leonard = Employee(name='Leonard', dept=dl)
    liz = Employee(name='Liz', dept=dl)
    maggie = Employee(name='Maggie', dept=dm)
    nadine = Employee(name='Nadine')

    db.session.add_all([df, dl, dm, leonard, liz, maggie, nadine])
    db.session.commit()
'''

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
