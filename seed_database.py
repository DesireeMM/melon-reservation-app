"""Script to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime, time

import crud
import model
import server

os.system("dropdb melon_res_db")
os.system("createdb melon_res_db")

model.connect_to_db(server.app)
model.db.create_all()

#create some users
for n in range(6):
    username = f'User{n}'
    password = crud.hash_password('test')

    new_user = crud.create_user(username, password)
    model.db.session.add(new_user)
    model.db.session.commit()