class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin Privileges:')
        for elem in self.privileges:
            print(elem)


class User:
    def __init__(self, first_name, last_name, gender, race, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.race = race
        self.birthday = birthday
        self.login_attempts = 0

    def describe_user(self):
        print(
            f'First Name: {self.first_name}\nLast Name: {self.last_name}\nGender: {self.gender}\nRace: {self.race}\nBirthday: {self.birthday}')

    def greet_user(self):
        print(f'Hi, {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, gender, race, birthday):
        super().__init__(first_name, last_name, gender, race, birthday)
        self.privileges = Privileges()
