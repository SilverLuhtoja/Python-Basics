class User:
    _count = 0
    #  Constructor takes it  class instance(by using self), and randomly named variables to assign to default values
    def __init__(self, name='nameless', city= 'no Location', age = 1):
        User._count += 1
        self.count = User._count
        self.first_name = name
        self.city = city
        self.__age = age
        print(f"Created a instance with name: {self.first_name}, city:{self.city}, age: { self.age}, INSTANCE NUMBER : {self.count}")
    def get_birth_year(self):
        return print(2021 - self.__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print('The age must be greater than 0.')




#  Cant create obj, cuz its missing 2 arguments
# user1 = User()


user1 = User('Aecio', "Tallinn")
user1.age = 10
print(user1.age)
