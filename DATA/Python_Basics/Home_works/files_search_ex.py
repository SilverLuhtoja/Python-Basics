name = input("Who do you want to search?").lower()

with open('user_dict.txt') as f:
    data_str = f.readline()

if data_str =='':
    data_str = '{}'

outer_dict = eval(data_str)
user_details = outer_dict.get(name)

if (user_details) is None:
    print(f"There is no user with that name {name}")
else:
    print(f"Ok, The user phone number is {user_details.get('phonenumber')} and city is {user_details.get('city')}")
