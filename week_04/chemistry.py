from formula import parse_formula

# Variable Initialization
# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def main():
    """
    Asks the user for the formula and sample_mass to compute the molar mass and number of moles of a chemical sample.
    It then calculates and prints the results.

    Parameters: None

    Returns: Nothing
    """
    # Variable Initialization
    valid_formula = False
    periodic_table = make_periodic_table()

    while not valid_formula:
        formula = input("What is the chemical formula for the molecule: ")
        sample_mass = float(input("What is the mass of your chemical sample in grams: "))
        valid_formula = validate_formula(formula, periodic_table)
    
    symbol_quantity_list = parse_formula(formula, periodic_table)
    total_molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    number_of_moles = sample_mass / total_molar_mass

    print(f"Grams per mole: {total_molar_mass:.5f}")
    print(f"Number of moles: {number_of_moles:.5f}")


def validate_formula(formula, periodic_table):
    """
    Validate the chemical formula entered by the user.

    Parameters:
        formula (str): The chemical formula entered by the user.
        periodic_table (dict): The dictionary representing the periodic table of elements.

    Returns:
        bool: True if the formula is valid, False otherwise.
    """
    for char in formula:
        if char.isalpha():
            if char not in periodic_table:
                print(f"Invalid element symbol: {char}")
                return False
        elif not char.isdigit():
            print(f"Invalid character in formula: {char}")
            return False
    return True


def make_periodic_table():
    """Create a dictionary representing the periodic table of elements.
    Each element in the dictionary has a chemical symbol as the key and a list containing the element name and atomic mass.

    Parameters: None

    Return: A dictionary representing the periodic table.
    """
    periodic_table_dict = {
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        "Ar": ["Argon", 39.948],
        "As": ["Arsenic", 74.9216],
        "At": ["Astatine", 210],
        "Au": ["Gold", 196.966569],
        "B": ["Boron", 10.811],
        "Ba": ["Barium", 137.327],
        "Be": ["Beryllium", 9.012182],
        "Bi": ["Bismuth", 208.9804],
        "Br": ["Bromine", 79.904],
        "C": ["Carbon", 12.0107],
        "Ca": ["Calcium", 40.078],
        "Cd": ["Cadmium", 112.411],
        "Ce": ["Cerium", 140.116],
        "Cl": ["Chlorine", 35.453],
        "Co": ["Cobalt", 58.933195],
        "Cr": ["Chromium", 51.9961],
        "Cs": ["Cesium", 132.9054519],
        "Cu": ["Copper", 63.546],
        "Dy": ["Dysprosium", 162.5],
        "Er": ["Erbium", 167.259],
        "Eu": ["Europium", 151.964],
        "F": ["Fluorine", 18.9984032],
        "Fe": ["Iron", 55.845],
        "Fr": ["Francium", 223],
        "Ga": ["Gallium", 69.723],
        "Gd": ["Gadolinium", 157.25],
        "Ge": ["Germanium", 72.64],
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Hf": ["Hafnium", 178.49],
        "Hg": ["Mercury", 200.59],
        "Ho": ["Holmium", 164.93032],
        "I": ["Iodine", 126.90447],
        "In": ["Indium", 114.818],
        "Ir": ["Iridium", 192.217],
        "K": ["Potassium", 39.0983],
        "Kr": ["Krypton", 83.798],
        "La": ["Lanthanum", 138.90547],
        "Li": ["Lithium", 6.941],
        "Lu": ["Lutetium", 174.9668],
        "Mg": ["Magnesium", 24.305],
        "Mn": ["Manganese", 54.938045],
        "Mo": ["Molybdenum", 95.96],
        "N": ["Nitrogen", 14.0067],
        "Na": ["Sodium", 22.98976928],
        "Nb": ["Niobium", 92.90638],
        "Nd": ["Neodymium", 144.242],
        "Ne": ["Neon", 20.1797],
        "Ni": ["Nickel", 58.6934],
        "Np": ["Neptunium", 237],
        "O": ["Oxygen", 15.9994],
        "Os": ["Osmium", 190.23],
        "P": ["Phosphorus", 30.973762],
        "Pa": ["Protactinium", 231.03588],
        "Pb": ["Lead", 207.2],
        "Pd": ["Palladium", 106.42],
        "Pm": ["Promethium", 145],
        "Po": ["Polonium", 209],
        "Pr": ["Praseodymium", 140.90765],
        "Pt": ["Platinum", 195.084],
        "Pu": ["Plutonium", 244],
        "Ra": ["Radium", 226],
        "Rb": ["Rubidium", 85.4678],
        "Re": ["Rhenium", 186.207],
        "Rh": ["Rhodium", 102.9055],
        "Rn": ["Radon", 222],
        "Ru": ["Ruthenium", 101.07],
        "S": ["Sulfur", 32.065],
        "Sb": ["Antimony", 121.76],
        "Sc": ["Scandium", 44.955912],
        "Se": ["Selenium", 78.96],
        "Si": ["Silicon", 28.0855],
        "Sm": ["Samarium", 150.36],
        "Sn": ["Tin", 118.71],
        "Sr": ["Strontium", 87.62],
        "Ta": ["Tantalum", 180.94788],
        "Tb": ["Terbium", 158.92535],
        "Tc": ["Technetium", 98],
        "Te": ["Tellurium", 127.6],
        "Th": ["Thorium", 232.03806],
        "Ti": ["Titanium", 47.867],
        "Tl": ["Thallium", 204.3833],
        "Tm": ["Thulium", 168.93421],
        "U": ["Uranium", 238.02891],
        "V": ["Vanadium", 50.9415],
        "W": ["Tungsten", 183.84],
        "Xe": ["Xenon", 131.293],
        "Y": ["Yttrium", 88.90585],
        "Yb": ["Ytterbium", 173.054],
        "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium", 91.224]
    }
    
    return periodic_table_dict


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """
    Compute and return the total molar mass of all the elements listed in symbol_quantity_list.
    
    Parameters:
        symbol_quantity_list: A list of lists representing chemical symbols and their quantities.
        periodic_table_dict: A dictionary representing the periodic table of elements.
    
    Returns:
        The total molar mass of all the elements in symbol_quantity_list.
    """
    total_molar_mass = 0
    
    for symbol_quantity in symbol_quantity_list:
        symbol = symbol_quantity[SYMBOL_INDEX]
        quantity = symbol_quantity[QUANTITY_INDEX]
        
        # Retrieve the atomic mass from the periodic table dictionary
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        
        # Multiply atomic mass by quantity and add to the total
        total_molar_mass += atomic_mass * quantity
    
    return total_molar_mass


if __name__ == "__main__":
    main()


# For exceeding the requirements I decieded to added a formula checker using the .isalpha and .isdigit string methods /
# to make sure that the formula is valid.
# If the user enters an element that is not in the periodic dictionary or a invalid symbol (not a digit) /
# it will let the user know and prompt them to enter again until a valid formula is entered.  