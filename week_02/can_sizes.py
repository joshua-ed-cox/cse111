import math

def main():
    """Goes through each can and uses functions to calculate 
    volume, surface area, storage efficency and then print that data.
    
    Parameters: None
    
    Returns: Nothing"""
    can_name = "#1 Picnic"
    can_cost = 0.28
    radius = 6.83
    height = 10.16
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#1 Tall"
    can_cost = 0.43
    radius = 7.78
    height = 11.91
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)
    
    can_name = "#2"
    can_cost = 0.45
    radius = 8.73	
    height = 11.59
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#2.5"
    can_cost = 0.61
    radius = 10.32
    height = 11.91
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#3 Cylinder"
    can_cost = 0.86
    radius = 10.79
    height = 17.78
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#5"
    can_cost = 0.83
    radius = 13.02
    height = 14.29
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)
    
    can_name = "#6Z"
    can_cost = 0.22
    radius = 5.40
    height = 8.89
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#8Z short"
    can_cost = 0.26
    radius = 6.83
    height = 7.62
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#10"
    can_cost = 1.53
    radius = 15.72
    height = 17.78
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#211"
    can_cost = 0.34
    radius = 6.83
    height = 12.38
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)
    
    can_name = "#300"
    can_cost = 0.38
    radius = 7.62
    height = 11.27
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

    can_name = "#303"
    can_cost = 0.42
    radius = 8.10
    height = 11.11
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficency = calculate_storage_efficency(volume, surface_area)
    cost_efficency = calculate_cost_efficency(volume, can_cost)
    display_data(can_name, storage_efficency, cost_efficency)

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

def calculate_cost_efficency(volume, can_cost):
    """Calculates the cost efficency of the can by dividing
    the volume by the can cost.
    
    Parameters: 
    volume
    can_cost
    
    Returns: 
    cost efficency"""
    return volume / can_cost

def display_data(can_name, storage_efficency, cost_efficency):
    """Displays the can name and it's storage_efficency
    to the user.
    
    Parameters: 
    can_name
    storage_efficency
    
    Returns: 
    nothing"""
    print(f"{can_name} has a storage efficency of {storage_efficency:.2f}, and a cost efficency of {cost_efficency:.2f}")

main()
