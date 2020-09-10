# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

#number = list(range(1,101))


#for x in list(range(1,101)):
#    string = ""

#    if x % 3 ==0:
#       string = string + "Fizz"
#    if x % 5 ==0:
#        string = string + "Buzz"
    #if x % 5 ==0 and x % 3 ==0:
        #string = string + "FizzBuzz"    
    
 #   print(x,string)

for number in range(1,101):
    if number % 3 ==0:
        print("Fizz")

    if number % 5 ==0:
        print("Buzz")

    if number % 3 ==0 and number % 5 ==0:
        print("FizzBuzz") 
    
    else:
        print(number)


    