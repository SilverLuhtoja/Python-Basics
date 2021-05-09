dict = {1: "one", 2: "two", 3: "three"}

# a.Use len() to print out its length.
print(len(dict))
# b.Using set-item operator [], add a new key-pair: 4:"four".
dict[4] = "four"
# c.Using get-item operator [], print out the value assigned to key 2.
print(dict[2])
# d.Using get-item operator [], print out value for unassigned key, like 10. What happens?
# print(dict[10])
# e.Using dictionary function get(key), replace the previous get-item operator [] and print out the value for key 10. What happens?
print(dict.get(10))
# f.Using dictionary function get(key, default), print out the value for key 10, this time setting default value to "unknown".
print(dict.get(10,'unknown'))
# g.Using dictionary function get(key, default), print out the value for key 3. Set default value to "unknown".
print(dict.get(3,'unknown'))
# h.Use pop() to print out value assigned to 2. Print out the dictionary after using pop().
print(dict.pop(2))
print(dict)
# i.Create a new dictionary {0: "zero"}.
new_dict = {0: 'zero'}
# Using update(), update main dictionary with values from the new dictionary.
dict.update(new_dict)
# Print out the main dictionary.
print(dict)
# j.Using clear(), clear the dictionary.
dict.clear()
print(dict)
