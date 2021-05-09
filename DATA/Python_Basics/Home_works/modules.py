# import random
# randomInt = random
import random as randomInt
#  MAKING RANDOM ID
def generate_id():
    id = ""
    for i in range(4):
        randomNr = round(randomInt.random() * 9)
        id += str(randomNr)
    return int(id)

id = generate_id()
print(id)

# from time import time
# import datetime
from datetime import datetime as time

print('Time is now :', time.now())