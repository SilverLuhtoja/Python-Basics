
"""
1 - Create Vehicle class with fields: name, type, color and value
and methods:description() that returns a string describing the vehicle.
    a.The Vehicle class initialization method should require name and price parameters and have default values for type and color.
    b.Create vehicles list.
    c.Write a loop that asks user 3 times for input regarding vehicle creation.
With each loop iteration user should provide name and price and should be asked if he wants to provide type and color.
If the user responds yes, he should be asked for the type and color. Once the input is collected, create new vehicle
based on the input and add it to the vehicles list.
    d.In a loop, print details of each car in the cars list.
"""
class Vehicle():
    def __init__(self, name, price, type="motorized vehicle", color='no color'):
        self.name = name
        self.value = price
        self.type = type
        self.color = color

    def description(self):
        if self.type != "motorized vehicle" and self.color != 'no color':
            return print(f"This car name is '{self.name}' and its price is set to {self.value} $. Its type is '{self.type}' and color is " \
                   f"{self.color}")
        else:
            return print(f"This car name is '{self.name}' and its price is set to {self.value} $.")

vehicle_list = []
def vehicle_creator(iterator):
    while True:
        for i in range(iterator):
            print(f"Creating vehicle nr {i+1}")
            name = input("Name: ")
            price= input("Price : ")
            while True:
                if price.isdigit():
                    break
                else:
                    price = input("Must contain only numbers: ")


            choice= input("Would you like to add type and color? Type yes/no to answer: ")
            if "y" in choice:
                type = input("The type of a vehicle : ")
                color= input("Color of a vehicle : ")
                vehicle_list.append(Vehicle(name,price,type,color))
            else:
                vehicle_list.append(Vehicle(name,price))

        for i in vehicle_list:
            i.description()

        exit()

vehicle_creator(1)
