# defined by def keyword

# passing arguments
def my_print(message):
    # returning the string
    return f'This is my function! And my message is  ---{message}---'

# x = input("Type your message")
# print(my_print(x))





def calculate(a,b,operator):
    calculation = 0
    if '+' in operator:
         calculation = a + b
    elif '-' in operator:
        calculation = a - b
    elif '*' in operator:
        calculation = a * b
    elif '/' in operator:
        calculation = a / b
    else:
        print("There is error in arguments")
        return None
    return (f"{a}{operator}{b}={calculation} ")
result = calculate(10,5,'*')
print(result)
