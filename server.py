from datetime import datetime
import json
from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud
from passlib.hash import argon2

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def view_homepage():
    """Display Melon Reservation Scheduling App homepage"""

    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def user_login():
    """Handle user login"""

    username = request.form.get("username")
    user_pw = request.form.get("password")

    current_user = crud.get_user_by_username(username)

    if not current_user:
        flash("Account does not exist. Please try again with a valid account.")
        return redirect("/")

    elif current_user and argon2.verify(user_pw, current_user.password):
        session["user_id"] = current_user.user_id
        return redirect("/dashboard")

    else:
        flash("Password incorrect. Please try again.")
        return redirect("/")

@app.route('/dashboard')
def view_dashboard():
    """View user dashboard"""

    current_user = crud.get_user_by_id(session.get("user_id"))
    reservations = current_user.reservations
    current_datetime = datetime.today()

    formatted_res = []
    for res in reservations:
        res_datetime = datetime.combine(res.date, res.start)
        if res_datetime > current_datetime:
            res_date = res.date.strftime('%B %d, %Y')
            res_time = res.start.strftime('%-I:%M %p')
            res_id = res.res_id
            formatted_res.append((res_date, res_time, res_id))
    
    upcoming_res = sorted(formatted_res)

    return render_template("dashboard.html",
                            current_user=current_user,
                            upcoming_res=upcoming_res)

@app.route('/search')
def view_search_form():
    """Display search form for reservations"""

    return render_template("search_form.html")

@app.route('/booking', methods=['POST'])
def display_booking_times():
    """Display possible reservation times"""

    search_date = request.form.get("date")
    search_start = request.form.get("start")
    search_end = request.form.get("end")

    open_bookings = crud.display_available_reservations(search_date, search_start, search_end)
    
    formatted_bookings = []
    for slot in open_bookings:
        formatted_time = slot.strftime('%-I:%M %p')
        formatted_bookings.append(formatted_time)

    return render_template("results.html",
                            res_date=search_date,
                            formatted_bookings=formatted_bookings)

@app.route('/make-reservation', methods=["POST"])
def handle_booking():
    """Handle a user making a reservation"""

    current_user_id = session.get("user_id")
    current_user = crud.get_user_by_id(current_user_id)
    desired_res = request.json.get("res_time")
    desired_date = request.json.get("res_date")

    res_date = datetime.strptime(desired_date, '%Y-%m-%d').date()
    res_time = datetime.strptime(desired_res, '%I:%M %p').time()

    black_out_dates = []
    for res in current_user.reservations:
        black_out_dates.append(res.date)

    if res_date not in black_out_dates:    
        new_res = crud.create_reservation(current_user_id, res_date, res_time)
        db.session.add(new_res)
        db.session.commit()
    else:
        return jsonify({
            "status": "You cannot book more than one reservation on the same day.",
            "redirect": "/search"
        })

    return jsonify({
        "status": f"You booked {desired_res}!",
        "redirect": '/dashboard'
    })


@app.route('/cancel-res', methods=['POST'])
def cancel_reservation():
    """Handle a user canceling a reservation"""

    target_res_id = request.json.get("res_id")
    target_res = crud.get_reservation_by_id(target_res_id)
    res_date = target_res.date
    db.session.delete(target_res)
    db.session.commit()

    return jsonify({
        "status": f"You have cancelled your reservation on {res_date}.",
        "redirect": '/dashboard'
    })


if __name__ == '__main__':
    connect_to_db(app)
    app.run('0.0.0.0', debug=True)
