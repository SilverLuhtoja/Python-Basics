# Ask the user name and phone nr
# Store/Save those names/numbers in  list
# Store names/numbers into dictionary with lists
# Print out: [Silver, 5656, Jass, 7777]

list_of_numbers = []

name1 = input("Type your name 1: ")
phone1 = input("type your number 1: ")

name2 = input("Type your name 2: ")
phone2 = input("type your number 2: ")

numbers_dict = {}
numbers_dict[name1] = phone1

list_of_numbers.append(numbers_dict)

name = f'{name2} - {phone2}'
list_of_numbers.append(name)

print(len(list_of_numbers))
print(list_of_numbers)
print(numbers_dict)
