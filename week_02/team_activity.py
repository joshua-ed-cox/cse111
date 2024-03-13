import math

def main():
    """Purpose: Cycle through each can and use functions to find the
    volume, surface, storage efficency and then print that data
    
    paramaters: none
    
    returns: nothing"""

    can_names = ["Picnic", "Tall", "2", "2.5", "3 Cylinder", "5", "6Z", "8Z short", "10", "211", "300", "303"]
    radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    for can_name, radius, height in zip(can_names, radii, heights):
        volume = compumte_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiecy = compute_storage_efficiecy(volume, surface_area)
        print_data(can_name, storage_efficiecy)

def compumte_volume(radius, height):
    """Purpose: Using the radius and height to find the volume of the 
    can (needed to calculate storage efficency)
    
    paramaters: radius and height
    
    returns: volume"""

    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    """Purpose: Using the radius and height to find the surface_area of the 
    can (needed to calculate storage efficency)
    
    paramaters: radius and height
    
    returns: surface_area"""

    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiecy(volume, surface_area):
    """Purpose: finds the storage efficiency of the can by dividing the volume
    over the surface_area
    
    paramaters: volume and surface_area
    
    returns: storage_efficiecy"""

    return volume / surface_area

def print_data(can_name, storage_efficiecy):
    """Purpose: print the can name and its storage efficiecy
    
    paramaters: can_name and storage_efficiecy
    
    returns: nothing"""

    print(f"{can_name} has a storage efficiecy of {storage_efficiecy:.2f}")

main()