import sqlite3
from models import user
from utils import db_ops as db
from datetime import datetime
from utils import date_time_manager as dt
from models import user

# elem = user.User("alistcolor")
# db.add_user(elem)

# elem = db.get_user_by_name("alistcolor")
# print(elem)
# elem.next_action = "unfollow"
# db.update_user(elem)


def get_new_users():
    conn = sqlite3.connect("../resources/insta.db")
    c = conn.cursor()
    time = dt.datetime_to_string(datetime.now())
    # print(time)
    # querry = "SELECT * FROM user WHERE status='new user' and next_action='get_followers' and next_date < '" + time + "' "
    querry = "SELECT * FROM user WHERE status='new user' and next_action='get_followers'  "
    # print(querry)
    c.execute(querry)
    raw_list = c.fetchall()
    print(raw_list)
    ret_list = list()
    for item in raw_list:
        ret_list.append(user.User(item))
    return ret_list

if __name__ == "__main__" :
    get_new_users()