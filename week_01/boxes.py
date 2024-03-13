import math

num_of_items = int(input("How many manufactered items are there: "))
items_per_box = int(input("How many items per box: "))

boxes_needed = math.ceil(num_of_items / items_per_box)

print(f"You need {boxes_needed} boxes to hold {num_of_items} items.")

