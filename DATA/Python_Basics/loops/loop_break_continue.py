while True:
    continue_in_program = input("Would you like to continue using the program? (YES/NO)")
    # if continue_in_program == "NO":
    #     break
    if continue_in_program == "YES":
        # JUMPS BACK TO BEGINING OF THE LOOP
        continue
    # BREAK THE LOOP ( WITH OUT IT, this LOop runs forever)
    break
print("Program ended")