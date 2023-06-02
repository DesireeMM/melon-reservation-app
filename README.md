# Melon Reservation Scheduler

Learn more about the developer on [LinkedIn](https://www.linkedin.com/in/desiree-morimoto-9470481b0/)

## Table of Contents
- [Project Description](#overview)
- [Technologies Used](#technologiesused)
- [Future Plans](#future)
- [Development Process](#process)

## Project Information

#### <a name="overview"></a>Description
This project is a simple service to help users schedule reservations for fancy melon tastings. There are a few restrictions on reservations:
- Users cannot have more than one reservation on any given day
- Reservation time slots are only available on the hour or half hour
- Reservations are exactly 30 minutes long
- Time slots can only be booked by one user
Users can sign in using their existing username and password.

#### <a name="technologiesused"></a>Technologies Used
- Python
- Flask
- HTML
- Jinja2
- CSS
- Bootstrap
- JavaScript
- AJAX
- PostgreSQL
- SQLAlchemy
- passlib

## <a name="future"></a>Future Features
This project had a quick turnaround time, but for future versions, I would include the following:

###### Account Creation
Right now, users must use login credentials that already exist in the database. I would like to allow users to create their own accounts.

###### fullcalendar.io API Integration
Right now, users can only view their reservations as a list. I'd like to be able to integration with fullcalendar.io's JavaScript API to display both user's reservations and potential booking times on a calendar.

###### User Interface Improvements
Right now, the web application interface is very plain. I would like to spend time improving the user interface to make the scheduling process more pleasant for the user.

###### React
I believe this project is a good candidate to use React. There are a lot of repeat components I used that I could attach functionality to, so I would implement React in the next version.

## <a name="process"></a>Development Process
1. My first step was to read the assignment and take down notes on the project requirements. I wanted to be thorough here to ensure my web application would meet the desired specifications.
2. From there, I was able to structure a data model for the backend database. I am most familiar with PostgreSQL databases and using SQLAlchemy as my ORM, so I chose to use them.
3. Next, I planned out my routes in advance, thinking about how a user might move through them. I wanted to use a framework I was familiar with, so I chose the Flask Python framework.
4. Once I had selected my database structure and framework, I created a database model in Python and corresponding CRUD functions in a separate file. I also knew I would need to create some test users in order to check the functionality of my web application, so I wrote a script to seed my database.
5. Once I had these components, I thought about the logic behind my booking system. I knew I would need to account for reservations made by the user, since they couldn't have more than one reservation on the same day. I also knew that I would need to take reservations made by other users into account, as more than one user could not book the same time. I accomplished this by utilizing lists and loops to get the data I needed.
6. After creating my routes in Python, I used HTML and Jinja2 to create the templates to be rendered.
7. After successfully displaying potential bookings, I used an AJAX fetch request to handle making a reservation. To check that it was successfully updating the database, I asked the following:
- Did the reservation show up on the user's dashboard?
- Did that time slot disappear from the available bookings displayed for the same search date?
- If a user attempted to make a reservation for that same day, would they be stopped?
8. Though it wasn't required, I wanted to add the option to cancel a reservation if a user's plans changed. I used another AJAX fetch request to handle deleting a booking. To check that it was successfully updating the database, I asked the following:
- Did the reservation disappear from the user's dashboard?
- Did that time slot open back up?
9. Lastly, I wanted to clean up the interface a bit, so I reworked some of my functions to included formatted dates and times. Additionally, I added some Bootstrap and CSS custom styling to improve the look of the site. As mentioned above, I would love to spend more time on the appearance to enhance the user experience.