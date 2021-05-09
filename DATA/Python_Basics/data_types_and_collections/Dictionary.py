# {} are needed to create the dictionary

# empty dictionary
phonebook = {}
# add items to it
phonebook["John"] = 1111111
phonebook["Bob"] = 22222222

print(phonebook)
print(phonebook["John"])
# Definition of the finished dictionary
phonebook2 = {
    "John" : 1111111,
    "Bob" : 2222222
}
print(phonebook2)

# To remove items from the dictionary, use .pop() and del keyword
del phonebook["John"]
print(phonebook)
phonebook.pop("Bob")
print(phonebook)

# .get() function of the dictionary returns the value under the key given as a parameters

letters = {
    "a" : 1,
    "b" : 2
}

print(letters.get('a'))
# We can specify further, as the second argument, the value that should be returned
# if the key does not exist in the dictionary.

print(letters.get('c', 'This key does not exist in letters'))

# TUPLE = A LIST THAT CANNOT BE MODIFIED AFTER ITS CREATION
#  () can be used to define it

tuple_1 = ()
# Short empty declaration
tuple_2 = ( "dog", "cat", 2000, 0.5, True)
# wont work
# tuple_2[2] = "Not any 2000"
print(tuple_2[2])


# SET - A NON-INDEXABLE AND UNORDERED COLLECTION
# its created by using the set() command
# set values are not repeatedd
# There is no access to elements,set elements don ot have indexes

# Creating set
animals = {"dog","cat", "elephant"}
#  add a new item
animals.add("mouse")
# add several items at once
animals.update(["bird", "horse"])
# add a same item again
animals.add('mouse')
#  There is no duplicated mouse there
print(animals )

#  Remove item,Python will throw an error id it is not in the set
animals.remove('cat')
print(len(animals) + 1 )

# Remove item, Python will NOT throw an error if it is not in the set
animals.discard("MINUJSDNu")
print(len(animals) + 1 )


# MUTABLE TYPES - LIST, COLLECTION, DICTIONARY
# IMMUTABLE TYPES - INT, FLOAT, BOOL,STR. ,TUPLE, FROZENSET