the_count =[1,2,3,4,5]
stocks = ["APPL","GOOG","TSLA"]
random_things = ["PUPPIES", 55, "Anthony Weiner",1/2, ["oh no", "A list inside a list"]]

# this for-loop goes through a list

for number in the_count:
    print("this is count", number)

# same as above

for stock in stocks:
    print("Stock ticker:", stocks)

    #for X in Y:
#we can go through mixed list too
# i called it i (short for Item) since i don't know what's in it

for i in random_things:
    print("here's a randon thing", i)

# we can also build list, start with an empty

people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# we can print them out
print(people)

#and remove them

people.remove("Sarah")

for person in people:
    print("person is", person)