from utils import date_time_manager as dt

class User:
    def __init__(self, name):
        self.name = name
        self.next_date = dt.get_next_time(False, True)
        self.status = "new user"
        self.next_action = "get_followers"

    def __init__(self, name, next_date, status, next_action):
        self.name = name
        self.next_date = next_date
        self.status = status
        self.next_action = next_action

    def __init__(self, param_list):
        self.name = param_list[0]
        self.next_date = param_list[1]
        self.status = param_list[2]
        self.next_action = param_list[3]

    def __str__(self):
        return str("[" + self.name + "  " + self.next_date + "  " + self.status + "  " + self.next_action + "]")
