
def main():
    print("Fuel Efficency Calculator\n")
    
    start_miles = int(input("Enter the starting odometer reading (miles): "))
    end_miles = int(input("Enter the ending odometer value (miles): "))
    gallons_used = float(input("Enter the amount of fuel used (gallons): "))

    miles_per_gallon = calculate_mpg(start_miles, end_miles, gallons_used)
    lp100k = calculate_lp100k(miles_per_gallon)

    print(f"You travel {miles_per_gallon:.1f} miles per gallon")
    print(f"You use {lp100k:.2f} liters per 100k kilometers")

def calculate_mpg(start_miles, end_miles, gallons_used):
    """Computes and returns the average amount of miles a vehicle 
    travels per gallon of fuel.
    
    Parameters:
    starting miles: An odometer value in miles
    ending_miles: An odometer value in miles
    gallons_used: A fuel amount in U.S. gallons
    
    Returns: fuel efficeny in miles per gallon"""

    miles_per_gallon = (end_miles - start_miles) / gallons_used
    return miles_per_gallon

def calculate_lp100k(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    
    Parameter: 
    mpg: A value in miles per gallon

    Return: The converted value in liters per 100km
    """
    lp100k = 235.215 / mpg
    return lp100k

main()

    



