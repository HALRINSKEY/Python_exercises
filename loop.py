import random

"""
list = ["walk","A","the","V"]
for  i, lists in enumerate(list):
    r = "{},{}".format(i, lists)
    print(r)


for i in range(25,51):
    print(i)

print("please number,range is 1 to 10")
r = random.randint(1,10)
print(r)
while True:
    i = input()
    if i == "q":
        break

    try:
        i = int(i)
    except ValueError:
        print("no")
        continue

    if i == r:
        print("yes")
        break
    else:
        print("no")
"""


x = [8,19,148,4]
y = [9,1,33,83]
result = []

for i in x:
    for j in y:
        formula = "{} * {} = {}".format(i,j,i*j)
        print(formula)
        result.append(i*j)

print(result)
