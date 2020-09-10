# Strings are surrounded by qouts
#both single('a') or double {""} or #"triple ("'")
# examples:"dinosars",2112,"i'm lovin' it"

kanye_quote = """My grearest pain in life is that I will never be able to see myself perform live."""
print(kanye_quote)

hamilton_quote = 'well, the word got around, they said \"this Kid\'s insane, man"'
print(hamilton_quote)

name = "Spencer Welsh"
orphan_fee = 200
teddy_bear_fee =121.80

total = orphan_fee + teddy_bear_fee

#print(name,"the total will be", total)
print(f"{name} the total will be ${total:.2f}")
