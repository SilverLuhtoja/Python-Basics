name = input('name to remove ? ')

with open('user_dict.txt') as f:
    data_str = f.readline()

if data_str == '':
    data_str = '{}'

outer_dict = eval(data_str)

user_details = outer_dict.pop(name, None)


if user_details is None:
    print("The user does not exist, try again!")
else:
    with open('user_dict.txt', mode='w') as f:
        f.writelines(str(outer_dict))
    print("User has been removed")