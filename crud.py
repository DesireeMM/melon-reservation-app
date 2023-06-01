"""CRUD operations for Melon Reservation Project"""

from datetime import timedelta, datetime, date, time
from model import (db,
                   User,
                   Reservation,
                   connect_to_db)
from passlib.hash import argon2

# creation functions
def create_user(username, password):
    """Create and return a new user"""

    user = User(username=username,
                password=password)

    return user

def create_reservation(user_id, date, start):
    """Create and return a new reservation"""

    reservation = Reservation(user_id=user_id,
                              date=date,
                              start=start)

    return reservation

# querying functions
def get_all_users():
    """Return a list of all users in the database"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user given their id"""

    return User.query.filter(User.user_id == user_id).first()

def get_user_by_username(username):
    """Return a user given their username"""

    return User.query.filter(User.username == username).first()

def get_all_reservations():
    """Return a list of current reservations"""

    return Reservation.query.all()

def get_reservation_by_id(res_id):
    """Return a reservation given its id"""

    return Reservation.query.get(res_id)

def get_reservations_by_date(search_date):
    """Return reservations booked on a particular date"""

    return Reservation.query.filter(Reservation.date == search_date).all()

def get_user_reservations(user_id):
    """Return a list of reservations made by a particular user"""

    return Reservation.query.filter(Reservation.user_id == user_id).all()

# updating functions
def update_reservation(res_id, new_date, new_start):
    """Modify a particular reservation"""

    target_res = get_reservation_by_id(res_id)
    target_res.date = new_date
    target_res.start = new_start
    db.session.commit()

    return Reservation.query.get(res_id)

def delete_reservation(res_id):
    """Delete a particular reservation"""

    target_res = get_reservation_by_id(res_id)
    db.session.delete(target_res)
    db.session.commit()

# relationship functions
def add_reservation(user_id, res_id):
    """Add a reservation to a user's list of reservations"""

    target_user = get_user_by_id(user_id)
    target_res = get_reservation_by_id(res_id)
    target_user.reservations.append(target_res)
    db.session.commit()

# helper functions
def hash_password(pw):
    """Hash a user's password for database storage"""
    hashed_pw = argon2.hash(pw)

    return hashed_pw

def convert_date(date_str):
    """Convert a date into a date object"""

    new_date = datetime.strptime(date_str, '%Y-%m-%d').date()

    return new_date

def convert_time(time_str):
    """Convert a time into a time object"""

    new_time = datetime.strptime(time_str, '%H:%M').time()
    
    return new_time

# reservation functions
def display_available_reservations(search_date, search_start=None, search_end=None):
    """Display reservations available on a given date"""

    # get a list of already booked times
    booked_reservations = get_reservations_by_date(search_date)
    booked_times = []
    for res in booked_reservations:
        combined_res_dt = datetime.combine(res.date, res.start)
        booked_times.append(combined_res_dt)

    # create a list of possible reservation times
    possible_res_times = []

    desired_date = convert_date(search_date)
    # determine what times we should display based on user search parameters
    if search_start:
        desired_start = convert_time(search_start)
        loop_start_time = datetime.combine(desired_date, desired_start)
    else:
        loop_start_time = datetime.combine(desired_date, time(00,00))

    interval = timedelta(minutes=30)

    if search_end:
        desired_end = convert_time(search_end)
        loop_end_time = datetime.combine(desired_date, desired_end)
    else:
        loop_end_time = datetime.combine(desired_date, time(23, 30))

    # add unbooked times to list of possible reservation times
    while loop_start_time < loop_end_time:
        if loop_start_time not in booked_times:
            possible_res_times.append(loop_start_time)
        loop_start_time = loop_start_time + interval

    return possible_res_times

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
