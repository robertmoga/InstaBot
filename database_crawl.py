import sqlite3
from models import user
from utils import db_ops as db

# elem = user.User("alistcolor")
# db.add_user(elem)

elem = db.get_user_by_name("alistcolor")
print(elem)
# elem.next_action = "unfollow"
# db.update_user(elem)


