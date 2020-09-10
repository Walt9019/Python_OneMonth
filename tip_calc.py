#Tip Cauclator 
#.15 .18 .20

print("I hope you enjoyed your meal")
# It took me a bit to figure out how to replace the $$, 
# I finialy came up with this, not sure if its the easies/Cleanest way
total = input("What was the total of your bill today? ")
total2 = total.replace("$","")
total3 = float(total2)
# .sprip() can be used to judt remove the '$' when actuly not replacing anything 
print(f"${total3:.2f}")

tip_15 = total3 * .15
tip_18 = total3 * .18
tip_20 = total3 * .20

print("Recommended Tip")
print(f"15%---${tip_15:.2f}")
print(f"18%---${tip_18:.2f}")
print(f"20%---${tip_20:.2f}")

print("Don't be Cheap!")


