
class User:
    first_name = ''
    last_name = ''
    age = 0
    city = ''

    # CONSTRUCTOR
    def __init__(self) :
        self.first_name = 'no name'
        self.last_name = 'no name'
        self.age = -1
        self.city = None
        pass

    def get_details(self):
        return f"Name:{self.first_name} {self.last_name} \nAge:{self.age}\nCity:{self.city}"


user1 = User()
user1.first_name = 'Silver'
user1.last_name = 'Luhtoja'
user1.age = 30

user1.city = 'aasmae'
user3 = User()
print(user1.get_details())
print(user3.get_details())
