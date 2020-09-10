#for number in [1,2,3,4,5,6,7,8,9,10]:
 #   print(number, "squared is", number * number)
for number in list(range(1,101)):
    print(number, "squared is", number * number)

google = list(range(4,99))

for google3 in google:
    #dont forget the :::::::::::::))
    print(google3)

    random_things = ["PUPPIES", 55, "Anthony Weiner",1/2, ["oh no", "A list inside a list"]]


animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0] 
print(first_animal)
third_animal = animals[3]

print("there are this many things", len(animals))
print("things is at", type(animals))

another_lsit = random_things[-1]
print(another_lsit)
print(type(another_lsit))