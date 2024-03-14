#Variable Initialization
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

EARTH_ACCELERATION_OF_GRAVITY = 9.8066500 # (meters per second squared)
WATER_DENSITY = 998.2000000               # (kilograms per cubic meter)
WATER_DYNAMIC_VISCOSITY = 0.0010016       # (pascal seconds)


def main():
    """
    This function calculates the pressure based on various parameters being the height of the water tower, 
    the height of the water tank walls, lengths of supply pipes, number of fittings, and pipe diameters and velocities.
    
    The function prompts the user to input values for these parameters and then computes the pressure.
    
    Parameters:
        None
        
    Returns:
        None
    """
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    psi = kpa_to_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi:.2f} pounds per square inch")


def water_column_height(tower_height, tank_height):
    """
    Calculate the total height of water in a tower including the height of the tower and the water tank walls.

    Parameters:
        tower_height (float): Height of the water tower in meters.
        tank_height (float): Height of the water tank walls in meters.

    Returns:
        float: Total height of water in the tower.
    """
    return tower_height + ((tank_height * 3) / 4)


def pressure_gain_from_water_height(height):
    """
    Calculate the pressure gain from the height of water.

    Parameters:
        height (float): Height of water column in meters.

    Returns:
        float: Pressure gain in kilopascals.
    """
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the pressure loss from friction within a pipe.

    Parameters:
        pipe_diameter (float): Diameter of the pipe in meters.
        pipe_length (float): Length of the pipe in meters.
        friction_factor (float): Friction factor of the pipe (unitless).
        fluid_velocity (float): Velocity of fluid flow in the pipe in meters per second.

    Returns:
        float: Pressure loss in kilopascals.
    """
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the pressure loss from fittings in a pipe.

    Parameters:
        fluid_velocity (float): Velocity of fluid flow in the pipe in meters per second.
        quantity_fittings (int): Number of fittings in the pipe.

    Returns:
        float: Pressure loss in kilopascals.
    """
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for fluid flow.

    Parameters:
        hydraulic_diameter (float): Hydraulic diameter of the pipe in meters.
        fluid_velocity (float): Velocity of fluid flow in the pipe in meters per second.

    Returns:
        float: Reynolds number (unitless).
    """
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / 0.0010016


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the pressure loss due to pipe diameter reduction.

    Parameters:
        larger_diameter (float): Larger diameter of the pipe in meters.
        fluid_velocity (float): Velocity of fluid flow in the pipe in meters per second.
        reynolds_number (float): Reynolds number (unitless).
        smaller_diameter (float): Smaller diameter of the pipe in meters.

    Returns:
        float: Pressure loss in kilopascals.
    """
    constant = (0.1 + (50 / reynolds_number)) * ((larger_diameter / smaller_diameter)**4 - 1)
    return (-constant * WATER_DENSITY * fluid_velocity**2) / 2000


def kpa_to_psi(kpa):
    """
    Convert the pressure from kPa to psi.

    Parameters:
        kPa (float): pressure in kilopascals.

    Returns:
       psi (float): pounds per square inch .
    """
    return kpa * 0.145038


if __name__ == "__main__":
    main()


#Submission Comment
#For exceeding the requirements I added multiple features including:
#Defining the global variables EARTH_ACCELERATION_OF_GRAVITY, WATER_DENSITY and WATER_DYNAMIC_VISCOSITY \ 
#Then using the variables in my calculations.
#I added a function to turn kPa into psi and displayed both kPa and psi in the main function.
#I created a test function for kpa_to_psi that tests and passes a wide range of scenarios.