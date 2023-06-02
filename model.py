"""Model for Melon Reservation Project"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# create User class
class User(db.Model):
    """A user on the scheduling application"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    # establish a relationship between users and their reservations
    reservations = db.relationship("Reservation", back_populates="user")

    def __repr__(self):
        
        return f"<User user_id: {self.user_id} username: {self.username}>"

# create Reservation class
class Reservation(db.Model):
    """A reservation on the scheduling application"""

    __tablename__ = "reservations"

    res_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    date = db.Column(db.Date, nullable=False)
    start = db.Column(db.Time, nullable=False)

    # establish a relationship between reservations and their user
    user = db.relationship("User", back_populates="reservations")

    def __repr__(self):

        return f"<Reservation res_id: {self.res_id} date: {self.date} time: {self.start}>"

def connect_to_db(flask_app, db_uri="postgresql:///melon_res_db", echo=False):
    """Function to connect to melon reservation database"""
    flask_app.config["SQLALCHEMY_DATABASE_URI"]= db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)