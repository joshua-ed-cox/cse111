import math
from datetime import datetime

# Variable Initalization
today = datetime.now()
buy_tires = ""
users_phone_num = ""

# Asks for tire dimensions and calculates volume
print("Tire Volume Calculator")
print()
width = float(input("Please enter the width of the tire in mm (e.g. 200): "))
aspect_ratio = float(input("Please enter the aspect ratio of the tire (e.g. 60): "))
diameter = float(input("Please enter the diameter of the tire in inches (e.g. 15): "))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"\n The aproximate volume of your tire in liters is: {volume:.02f}")

# Asks the user if they would like to purchase tires and if "yes" gathers phone number to put in volumes.txt
while buy_tires.lower() not in ["yes", "no"]:
    print(f"\nTire Dimensions: Width-{width}, Aspect Ratio-{aspect_ratio}, Diameter-{diameter}")
    buy_tires = input("Would your like to buy tires with the following dimensions today (Yes/No): ")
    if buy_tires.lower() not in ["yes", "no"]:
        print("That is not an accepted field, please enter (Yes/No)")

if buy_tires.lower() == "yes":
    users_phone_num = input("\nGreat! Please enter your phone number so we can authorize your purchase: ")
    print("Thank you for shopping with us, have a great day!")
else:
    print("\nThank you for using our calculator, have a great day!")

# adds tire dimensions and phone # (if applicable) to volumes.txt
with open("week_01/volumes.txt", "at") as volumes_file:
    print(f"{today:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.02f}, {users_phone_num}", file=volumes_file)

# Submission Comment
# For exceeding the requirements I added the option to purchase tires with the given dimensions and added error handling to the yes/no input.
# If yes, the user is asked for their phone # which is appended to the volumes.txt document. 
