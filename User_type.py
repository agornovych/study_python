class UserLevel():
    us_dict = {"Admin": 4, "Operator": 3, "Dispatcher": 2, "Guest": 1}

    def __init__(self, user_level):
        if user_level in self.us_dict:
            self.u_level = user_level
        else:
            print("Wrong user type!")
            self.u_level = "Guest"

    def diff(self, level1, level2):
        return self.us_dict[level1] - self.us_dict[level2]

    def __lt__(self, user):
        return True if self.diff(self.u_level, user.u_level) < 0 else False

    def __le__(self, user):
        return True if self.diff(self.u_level, user.u_level) <= 0 else False

    def __eq__(self, user):
        return True if self.diff(self.u_level, user.u_level) == 0 else False

    def __ge__(self, user):
        return True if self.diff(self.u_level, user.u_level) >= 0 else False

    def __gt__(self, user):
        return True if self.diff(self.u_level, user.u_level) > 0 else False

    def __repr__(self):
        return "UserLevel({})".format(self.u_level)

    def __str__(self):
        return self.u_level


if __name__ == "__main__":
    need_level = UserLevel("Operator")
    print("need level: {}".format(need_level))
    user_level = UserLevel("Operator")
    print("user: {}".format(user_level))
    if user_level >= need_level:
        print("Access enabled!")
    else:
        print("Access denied!")