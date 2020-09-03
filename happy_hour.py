import random

food1 = ["steak","bacon","sasuage","pork chop", "chicken"]

food2 = ["eggs","maders","onions","taters","fruit"]

food3 = ["corn on the cob","salad","garlic bread","pea salad"]

cooked = ["grill","open fire","stove","microwave"]

drink = ["beer","water","coke","coffee"]

desert = ["cookie","cake","jello","pie"]

random_food1 = random.choice(food1)
random_food2 = random.choice(food2)
random_food3 = random.choice(food3)
random_cooked = random.choice(cooked)
random_drink = random.choice(drink)
random_desert = random.choice(desert)


print(f"what's for dinner Mom?  Johnnie, we are having {random_food1} with {random_food2} and {random_food3} prepared on the {random_cooked} with {random_drink} and {random_desert} to finish with desert.")