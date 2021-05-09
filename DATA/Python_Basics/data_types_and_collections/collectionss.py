# [] to creata a list
alphabet = []
print(f"Current length of the alphabet variable : {len(alphabet)}")

# .append() function is used to add items to end of the list
alphabet.append('a')
alphabet.append('b')
alphabet.append("c")
print(f"Alphabet: {alphabet} (length: {len(alphabet)})")

# Items in the list are indexed (counted) from 0!!!
print(f"first letter of the alphabet : '{alphabet[0]}' .")

# .extend() function allows me to add multiuple items to  the list at the same time
alphabet.extend(["f", "d", "g", "e"])
print(f"Alphabet (confused) : {alphabet} (length: {len(alphabet)})")
# .sort() function when we want to sort items in a given list
# alphabet.sort()
# print(f"Alphabet (sorted): {alphabet} (length: {len(alphabet)})")

# We use the sorted() function when we want to sort elements in a given list without changing the list itself -
# a new, sorted list will be returned, while the old one will remain intact.

sorted_alphabet = sorted(alphabet)
print(f"Alphabet (sorted) : {sorted_alphabet}, alphabet(unsorted) : {alphabet}")

# Slicing List
users = ["Alice", "Bob", "Chris", "John"]
print(users)
print(users[0:3])
print(users[1:2])
print(users[2])
print(users[1:])


sortThat = input("What to sort?")
# sortThat.split(' ').sort()
splitThat = sortThat.split(' ')
splitThat.sort()
print(f"List made from input and sorted: {splitThat}")