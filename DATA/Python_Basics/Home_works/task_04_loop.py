a = int(input(('Integer a: ')))
b = int(input(('Integer b: ')))

if a > b:
    print("Job Finished")
    exit()

sum = 0
# a to b, b number not included, that's why we need +1
for i in range(a,b+1):
    sum += i

print(sum)

