from User import User


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin Privileges:')
        for elem in self.privileges:
            print(elem)


class Admin(User):
    def __init__(self, first_name, last_name, gender, race, birthday):
        super().__init__(first_name, last_name, gender, race, birthday)
        self.privileges = Privileges()
