"""
As you have the files writer.py, search.py and delete.py. Follow the recommendations.
1- Make your program in one file called phone_books.py:
    -Create functions for writing, searching and deleting instead of having those in different files.
    -Ask the user what He wants to do (insert, search, delete, finish the program)
2- Create a function read_file(), this function can be used for other functions. It means you dont need
to repeat the reading process anymore, instead of you can just use that function.
3- Make the search able to find phone books by city. If you have more than one user in the same city, show them.
"""
outer_dict = {}
name = ''
phonenumber= ''
city = ''

def read_file():
    with open('user_dict.txt') as f:
        data_str = f.readline()

    if data_str == '':
        data_str = '{}'

    outer_dict = eval(data_str)
    return outer_dict, data_str


read_file()
def write():
        name = input("Please provide your name: ").lower()
        phonenumber = input("Provide number : ")
        city = input("City your are staying: ")
        inner_dict = {
            "phonenumber": phonenumber,
            "city": city
        }

        outer_dict[name] = inner_dict

        with open('user_dict.txt', mode="w+") as file:
            file.write(str(outer_dict))

        return outer_dict.name, outer_dict.phonenumber, outer_dict.city
def search():
        name = input("Who do you want to search?").lower()
        user_details = outer_dict.get(name)

        if (user_details) is None:
            print(f"There is no user with that name {name}")
        else:
            print(f"Ok, The user phone number is {user_details.get('phonenumber')} and city is {user_details.get('city')}")

def delete():
        read_file()
        name = input('name to remove ? ')
        user_details = outer_dict.pop(name, None)

        if user_details is None:
            print("The user does not exist, try again!")
        else:
            with open('user_dict.txt', mode='w') as f:
                f.writelines(str(outer_dict))
            print("User has been removed")

def init():
    print(outer_dict)
    flag = False
    user_action = input("What would you like to do (insert,search,delete,exit) ?  ")
    actions =['insert', 'search','delete', 'exit']

    while True:
        if user_action in 'insert' and flag == True:
            write()
            print(f"contact {name} with number {phonenumber} and city {city} have been added to phonebook")
            print(f"{outer_dict}")
            continue
        if user_action in 'search':
            print(f"Searching for {name}")
            search()
        if user_action in 'delete':
            delete()
            print(f"contact {name} deleted")
        if user_action in 'exit':
             print(f"Program is closing")
             exit()
        if user_action not in actions:
            print(f"Sorry, this '{user_action}' command have no use.")
            user_action = input(" You can only use (insert,search,delete,exit) ?")


init()
