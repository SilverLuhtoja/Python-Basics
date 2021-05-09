print("Would you like a pancake? \nWrite Yes or No!")


def question():
    answer = input("Answer: ").lower()
    if answer.startswith("y"):
        print("Enjoy your pancake!")
    elif answer.startswith("n"):
        print("But pancakes are good!")
    else:
        print("Please answer yes or no! Thank you!")
        question()


question()
