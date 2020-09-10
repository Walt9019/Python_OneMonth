#states =['New York', 'Pennsylvania', 'California']
#states =['NY','PA','CA']

#states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}


#print(states['NY'])

#people =["Spencer", "Josh", "Kevin"]

#print(type(states))
#print(type(people))

#print the key print(states.keys())
#print only values print(states.values())

#add to a list
#states['FL'] = 'FLordia'
#print(states)

#Dictonarys and list can be insid eone another 

animal_sounds = {
    "cat": ['meow', 'purr'],
    "dog": ["woof", "bark"],
    'fox': []

}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown'}
chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown'}
sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown'}

people = [mattan, chris, sarah]

print(people)

for person in people:
    print(person.get('height'))