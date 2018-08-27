import sqlite3
from models import user


def add_user(user):
    conn = sqlite3.connect("resources/insta.db")
    querry = "INSERT INTO user VALUES (?, ?, ?, ?)"
    c = conn.cursor()
    c.execute(querry, (user.name, user.next_date, user.status, user.next_action))
    conn.commit()
    c.close()
    conn.close()

def update_user(usr):
    conn = sqlite3.connect("resources/insta.db")
    querry = "UPDATE user SET next_date=?, status=?, next_action=? WHERE name='"+usr.name+"'"
    c = conn.cursor()
    c.execute(querry, (usr.next_date, usr.status, usr.next_action))
    conn.commit()
    c.close()
    conn.close()

def get_user_by_name(name):
    conn = sqlite3.connect("resources/insta.db")
    querry = "SELECT * FROM user WHERE user.name='"+name+"'"
    c = conn.cursor()
    c.execute(querry)
    data = c.fetchall()
    c.close()
    conn.close()
    print(data)
    new_user = user.User(data[0][0], data[0][1], data[0][2], data[0][3])
    return new_user
