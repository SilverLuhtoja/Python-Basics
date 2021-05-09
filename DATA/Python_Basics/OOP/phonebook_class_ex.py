
class Contact:
    def __init__(self, name, number, city):
        self.name = name
        self.number = number
        self.city = city
        self.first_name = self.name.split(" ")[0]
        self.last_name = self.name.split(" ")[-1]
    def get_contact_details(self):
        return "{" + f"{self.name} - {self.number} - {self.city}" + "}"
