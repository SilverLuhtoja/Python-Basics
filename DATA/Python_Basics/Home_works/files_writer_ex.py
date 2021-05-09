# Ask the user for name/phonenumber/city
# Store his/her data into a file using this

name = input("Please provide name: ").lower()
phonenumber = input("Provide number : ")
city = input ("City your are staying: ")
inner_dict = {
    "phonenumber" : phonenumber,
    "city" : city
}


with open('user_dict.txt') as f:
    data_str = f.readline()
    print("Data saved!")

if data_str == '':
    data_str = '{}'

outer_dict = eval(data_str)
outer_dict[name] = inner_dict

with open('user_dict.txt', mode="w+") as file:
    file.write(str(outer_dict))

