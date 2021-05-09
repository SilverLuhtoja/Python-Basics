class User:
    def __init__(self, name, city, age = 1):
        self.first_name = name
        self.city = city
        self._age = age
    @property
    def name(self):
        return f"{self.first_name}"

class Programmer(User):
    def __init__(self, name, city, age, languages= [ ]):
        super().__init__(name="jeff",city= "tallinn",age= 18)
        self.languages = languages

programmer1 = Programmer('', '', 10 , languages=['Python', 'Java'])

print("the programmer name is : ", programmer1.name, programmer1.city, programmer1._age)
