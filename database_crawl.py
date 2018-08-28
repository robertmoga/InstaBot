import sqlite3
from models import user
from utils import db_ops as db
from datetime import datetime
from utils import date_time_manager as dt

# elem = user.User("alistcolor")
# db.add_user(elem)

# elem = db.get_user_by_name("alistcolor")
# print(elem)
# elem.next_action = "unfollow"
# db.update_user(elem)


def get_users_profile_crawling():
    conn = sqlite3.connect("resources/insta.db")
    c = conn.cursor()
    time = dt.datetime_to_string(datetime.now())
    querry = "SELECT * FROM user WHERE status='new user' and next_action='get_followers' and next_date < '" + time + "' "
    print(querry)
    c.execute(querry)
    list = c.fetchall()
    print(list)

get_users_profile_crawling()