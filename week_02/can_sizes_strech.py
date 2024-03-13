import math

def main():
    """Goes through each can and uses functions to calculate 
    volume, surface area, storage efficency and then print that data.
    
    Parameters: None
    
    Returns: Nothing"""

    # Variable Initialization
    greatest_storage_efficency = 0
    greatest_cost_efficency = 0
    best_storage_can = ""
    best_cost_can = ""

    can_sizes = [
        "#1 Picnic",
        "#1 Tall",
        "#2",
        "#2.5",
        "#3 Cylinder",
        "#5",
        "#6Z",
        "#8Z short",
        "#10",
        "#211",
        "#300",
        "#303"
    ]

    radii = [
        6.83,   # Radius for "#1 Picnic"
        7.78,   # Radius for "#1 Tall"
        8.73,   # Radius for "#2"
        10.32,  # Radius for "#2.5"
        10.79,  # Radius for "#3 Cylinder"
        13.02,  # Radius for "#5"
        5.40,   # Radius for "#6Z"
        6.83,   # Radius for "#8Z short"
        15.72,  # Radius for "#10"
        6.83,   # Radius for "#211"
        7.62,   # Radius for "#300"
        8.10    # Radius for "#303"
    ]

    heights = [
        10.16,  # Height for "#1 Picnic"
        11.91,  # Height for "#1 Tall"
        11.59,  # Height for "#2"
        11.91,  # Height for "#2.5"
        17.78,  # Height for "#3 Cylinder"
        14.29,  # Height for "#5"
        8.89,   # Height for "#6Z"
        7.62,   # Height for "#8Z short"
        17.78,  # Height for "#10"
        12.38,  # Height for "#211"
        11.27,  # Height for "#300"
        11.11   # Height for "#303"
    ]

    costs = [
        0.28,   # Cost for "#1 Picnic"
        0.43,   # Cost for "#1 Tall"
        0.45,   # Cost for "#2"
        0.61,   # Cost for "#2.5"
        0.86,   # Cost for "#3 Cylinder"
        0.83,   # Cost for "#5"
        0.22,   # Cost for "#6Z"
        0.26,   # Cost for "#8Z short"
        1.53,   # Cost for "#10"
        0.34,   # Cost for "#211"
        0.38,   # Cost for "#300"
        0.42    # Cost for "#303"
    ]

    # Finding volume, surface_area, storage_efficency and cost_efficency for each can
    for can_name, radius, height, cost in zip(can_sizes, radii, heights, costs):
        volume = calculate_volume(radius, height)
        surface_area = calculate_surface_area(radius, height)
        storage_efficency = calculate_storage_efficency(volume, surface_area)
        cost_efficency = calculate_cost_efficency(volume, cost)
        display_data(can_name, storage_efficency, cost_efficency)
        
        # Finding the greatest storage/cost efficency of all cans
        if storage_efficency > greatest_storage_efficency:
            greatest_storage_efficency = storage_efficency
            best_storage_can = can_name
        if cost_efficency > greatest_cost_efficency:
            greatest_cost_efficency = cost_efficency
            best_cost_can = can_name

    display_efficent_can(greatest_storage_efficency, best_storage_can, greatest_cost_efficency, best_cost_can)
    
def calculate_volume(radius, height):
    """Calculates the volume of the can
    which is needed to calculate storage efficency.
    
    Parameters: 
    Radius
    Height
    
    Returns: 
    Volume"""
    return math.pi * radius**2 * height

def calculate_surface_area(radius, height):
    """Calculates the surface area of the can
    which is needed to calculate storage efficency.
    
    Parameters: 
    Radius
    Height
    
    Returns: 
    Surface Area"""
    return 2 * math.pi * radius * (radius + height)

def calculate_storage_efficency(volume, surface_area):
    """Calculates the surface area of the can by dividing
    the volume by the surface area.
    
    Parameters: 
    volume
    surface_area
    
    Returns: 
    storage_efficency"""
    return volume / surface_area

def calculate_cost_efficency(volume, cost):
    """Calculates the cost efficency of the can by dividing
    the volume by the can cost.
    
    Parameters: 
    volume
    can_cost
    
    Returns: 
    cost efficency"""
    return volume / cost

def display_data(can_name, storage_efficency, cost_efficency):
    """Displays the can name and it's storage_efficency
    to the user.
    
    Parameters: 
    can_name
    storage_efficency
    
    Returns: 
    nothing"""
    print(f"{can_name} has a storage efficency of {storage_efficency:.2f}, and a cost efficency of {cost_efficency:.2f}")

def display_efficent_can(greatest_storage_efficency, best_storage_can, greatest_cost_efficency, best_cost_can):
    """Displays the can with the best storage and cost efficiency.
    
    Parameters: 
    greatest_storage_efficiency
    best_storage_can
    greatest_cost_efficiency
    best_cost_can
    
    Returns: 
    nothing"""
    print(f"\nThe can with the best storage efficency is {best_storage_can} with a score of {greatest_storage_efficency:.2f}")
    print(f"The can with the best storage efficency is {best_cost_can} with a score of {greatest_cost_efficency:.2f}")

main()