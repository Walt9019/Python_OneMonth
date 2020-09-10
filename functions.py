def greet(name):
    return f"Hey {name}!"

print(greet('Spencer'))
print(greet('Josh'))

def concatemate(word_one, word_two):
    return word_one + word_two

print(concatemate('Spencer ', 'Seth'))

def age_in_dog_years(age):
    return age * 7

print(age_in_dog_years(28))

print(concatemate(word_two='Spencer', word_one="Josh"))

name = "Spencer"

def print_diffrent_name():
    name = "Chris"
    print(name)

print(name)
print_diffrent_name()
print(name)

# Creat/Define a new function
# upper case and revers

def uppercase_and_reverse(word):
    uppercase_text = word.upper()
    revese_and_uppercase_text = uppercase_text[::-1]
    return revese_and_uppercase_text
    
print(uppercase_and_reverse("banna"))
