''''

height = int(input("height:")) >= 150
weight = float(input("weight:")) < 180
print(height,weight)
if height and weight :
    print("Fasten seat belts!")
else:
    print("I'm sorry, but you cant enjoy ride!")
'''

# Write a program which, based on the variables:
# amount - amount (float) and number of installments - number_of_installments (int),
# will calculate the monthly loan installment and write it to the console. The parameters have restrictions:


amount = float(input('Amount:'))
installments = int(input('Number of installments'))


if 100.00 > amount or amount > 10000.00:
    amount = 5000
    print("Amount set to  5000")
if installments < 6 or installments > 48:
    installments = 36
    print('Installment set to 36')

loan_interest = 0
monthly_payments = 0
if installments >= 6 and installments<=12:
    loan_interest = 1.025
    monthly_payments = (loan_interest * amount) / installments
    print(f"{monthly_payments} is monthly payment and total payment is {loan_interest*amount}")
elif installments >= 13 and installments<=24:
    loan_interest = 1.05
    monthly_payments = (loan_interest * amount) / installments
    print(f"{monthly_payments} is monthly payment and total payment is {loan_interest*amount}")
else:
    loan_interest = 1.1
    monthly_payments = (loan_interest * amount) / installments
    print(f"{monthly_payments} is monthly payment and total payment is {loan_interest*amount}")

