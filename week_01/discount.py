from datetime import datetime

# Get the current date and day of the week
today = datetime.now()
day_of_week = today.weekday()

# Initialize variables
discount_day = False
earned_discount = False
item_cost = -1
sub_total = 0

# Check if today is Tuesday or Wednesday
if day_of_week == 1 or day_of_week == 2:
    discount_day = True

# Loop to input item costs until user enters 0
while item_cost != 0:
    item_cost = float(input("Please Enter the cost of your item (Enter 0 to finish): "))
    if item_cost != 0:
        sub_total += item_cost

# Calculate discount, if applicable
if discount_day and sub_total >= 50:
    discount = sub_total * .1
    sub_total -= discount
    earned_discount = True
else:
    additional_amount_needed = 50 - sub_total

# Calculate sales tax
sales_tax = sub_total * .06
sub_total += sales_tax

# Print discount information
if discount_day and earned_discount:
    print(f"\nYou saved ${discount:.02f} on your purchase today!")
elif discount_day and additional_amount_needed > 0:
    print(f"\nYou can earn a 10% discount if you spend ${additional_amount_needed:.02f} more.")
else:
    print("You did not earn a discount today.")

# Print sales tax and total
print(f"Your sales tax is: ${sales_tax:.02f}")
print(f"Your total is: ${sub_total:.02f}")
print("\nThank you for shopping with us!")



