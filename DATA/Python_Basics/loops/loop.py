# nr = int(input("Give nr : "))
# count = 1
#
# while count < nr:
#     print(count)
#     count *= 2

# Ask the users how many user's weights. He wants to have the average.
# type all of those average
# Print out the average of their weights

number_of_users=int(input("How many users average you want to weigh ? "))
i = 1
sum_of_weights = 0
collection_of_weights = {}
while i <= number_of_users:
    weight=float(input(f"Weight of person {i} is:"))
    sum_of_weights += weight
    collection_of_weights[f"person{i}"] = round(weight)
    i += 1
average = sum_of_weights / number_of_users
print(f"Average from {number_of_users} people is { round(average)} from \nVisual overview: {collection_of_weights}")

