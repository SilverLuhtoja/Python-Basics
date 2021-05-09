import json
class Contact:
    def __init__(self, name, number, city):
        self.name = name
        self.number = number
        self.city = city
        self.first_name = self.name.split(" ")[0]
        self.last_name = self.name.split(" ")[-1]
    def get_contact_details(self):
        return   {
            'name' : self.name,
            'number' : self.number,
            'city' : self.city
        }


def read_file(file_name):
    with open(f"{file_name}") as f:
        data = f.readline()
        # eval_data = eval(data)
        if data == '':
            data ='{}'
        # data_str = eval(data)
        # return data_str

# outerDict = read_file('oop_test_file.txt')


def add_contact():
    name=input("Name: ")
    number=input("number: ")
    city=input("city: ")
    person = Contact(name,number,city)
    # add name and info to dictionary, next write function writes it to the file
    info = person.get_contact_details()
    with open('oop_test_file.txt', mode='a') as file:
        file.write(str(info))
        # this line is not working
        # json.dumps(outerDict,file)
        print(f"Contact added to the contact file")

# add_contact()

test_json = {
    'persons' : [{
        'name': 'kalle',
        'number': '211222',
        'city': 'rapla'
    },
    {
        'name': 'kalle',
        'number': '211222',
        'city': 'rapla'
    }]
}
print(test_json)

