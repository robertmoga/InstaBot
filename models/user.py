
class User:
    def __init__(self, name ):
        self.name = name
        self.next_date = self.update_datetime()
        self.status = "new user"
        self.next_action = "follow"

    def __init__(self, name, next_date, status, next_action):
        self.name = name
        self.next_date = next_date
        self.status = status
        self.next_action = next_action

    @staticmethod
    def update_datetime():
        #fill in implementation details
        return "0-0-2018:00-00-00"

    def __str__(self):
        print(self.name + "  " + self.next_date + "  " + self.status + "  " + self.next_date)