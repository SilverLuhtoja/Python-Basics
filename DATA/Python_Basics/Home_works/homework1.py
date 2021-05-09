"""
1- Write an application that: (IF)
a.Asks user for a number from 1 to 7.
b.If the number provided by user is smaller than 1, prints out “There are no negative number days!”.
c.For input number 1, prints out “You chose Monday”.
d.If the number provided by user is greater than 7, prints out “There are only 7 days in a week!”.
"""

# weekdays= ["Monday", "Tuesday", "Wednesday","Thursday","Friday", "Saturday", "Sunday"]
# a= int(input("Give a number : "))
# if(a<1):
#     print("There are no negative numbers days")
# elif a < 7:
#     print(f"You Chose {weekdays[a - 1]}")
# else:
#     print("There are only 7 days in a week")


'''
2- Ask the user to type 3 numbers. Print out which is the greatest and lowest.
'''
# numbers_typed = []
# greatest = 0
# lowest = 0
# for i in range(3):
#     a=int(input(f"Provide number {i+1}  "))
#     numbers_typed.append(a)
#     print(list)
#     if(a > greatest):
#         greatest = a
#         lowest = a
#     elif a < lowest :
#         lowest=a
#
# print(f"Greatest is :{greatest} Lowest is :{lowest}")

'''
3- A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''
# years_of_work = int(input("Years you have worked with us :  "))
# worker_salary = int(input("Your current salary: "))
#
# if years_of_work > 5:
#     print(f"Your bonus will be {worker_salary * 0.05}$")
# else:
#     print("Sorry, No bonus for you. More work,work,work.")

'''
4- Take input of age of 3 people by user and determine oldest and youngest among them.
'''
# ages= []
# for age in range(3):
#     number = int(input(f"How old are you (person{age+1})? "))
#     ages.append(number)
#
# print(f"Oldest {max(ages)} and Youngest {min(ages)}")

'''
5- Write an application that: (WHILE)
a.Asks user for an input in a loop and prints it out.
b.If the input is equal to “exit”, program terminates printing out provided input and “Done.”.
c.If the input is equal to “exit-no-print”, program terminates without printing out anything.
d.If the input is equal to “no-print”, program moves to next loop iteration without printing anything.
e.If the input is different than “exit”, “exit-no-print” and “no-print”, program repeats.
'''

# while True:
#     user_input = input("Type your input: ")
#     if user_input == "exit":
#         print(user_input, "Done")
#         break
#     if user_input == "exit-no-print":
#         break
#     if user_input == "no-print":
#         continue
#     else:
#         print(user_input)
#         continue

'''
6- Write an application that prints a sum of all numbers between 20 and 30.
'''
# sum_of_numbers = 0
# list_of_numbers = []
# #  30 is not included without +1
# for i in range(20, 30 + 1):
#     sum_of_numbers += i
#     list_of_numbers.append(i)
#
# print(list_of_numbers)
# print(f"Sum of all numbers from 20 to 30 is {sum_of_numbers}")

'''
7 - Ask the user to type numbers separated by comma (4,-8,2,-9,1). Print out how many numbers are positive and how many are negative.
'''
# typed_numbers = eval(input("Type numbers separated by comas:  "))
# print(typed_numbers)
# positive_count = 0
# negative_count = 0
# for i in typed_numbers:
#     if i < 0:
#         negative_count += 1
#     elif i > 0:
#         positive_count += 1
#     else:
#         continue
#
#
#
# print(f"There is {positive_count} positive numbers and {negative_count} negative numbers ")


'''
8- Given a list of numbers, return True if first and last number of a list is same
'''

# list_of_numbers = [1,23,56,78,9,23,1]
# def check_first_and_last(list):
#     if list[0] == list[-1]:
#         return True
#     else:
#         return False
#
# returned_value = check_first_and_last(list_of_numbers)
# print(returned_value)

'''
9- Ask the user to type 5 fruits names, print out how many names were double and a list of non double fruit names.
'''

def fruity():
    # Create empty list
    fruits=[]
    # Create variable for counting doubles
    double_count = 0
    # loop 5 times
    for fruit in range(5):
        # Get fruit
        fruit = input("Give me a fruit : ")
        # If user fruit is not in a created fruits list, Add it
        if fruit not in fruits:
            fruits.append(fruit)
        # Otherwise dont add the fruit to list, instead add it to count
        else:
            double_count += 1;
    #  Print counted fruits and fruits list item with no dublicates
    print(f"{double_count} names were double and a list of non double fruit names is: {fruits}")

fruity()
# Create empty list
fruits=[]
# Create variable for counting doubles
double_count = 0
# loop 5 times
for fruit in range(5):
    # Get fruit
    fruit = input("Give me a fruit : ")
    # If user fruit is not in a created fruits list, Add it
    if fruit not in fruits:
        fruits.append(fruit)
    # Otherwise dont add the fruit to list, instead add it to count
    else:
        double_count += 1;
#  Print counted fruits and fruits list item with no dublicates
print(f"{double_count} names were double and a list of non double fruit names is: {fruits}")