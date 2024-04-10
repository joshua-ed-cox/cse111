import csv
from datetime import datetime

# Constants for file and dictionary 
PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
QUANTITY_INDEX = 1

# File paths
PRODUCTS_FILE = "products.csv"
REQUEST_FILE = "request.csv"

# Store constants
STORE_NAME = "Inkom Emporium"
SALES_TAX = .06 


def main():
    """Reads products and requests, and prints requested items."""
    
    try:
        # Variable initialization
        subtotal = 0
        total_quantity = 0
        current_date_and_time = datetime.now()

        # List to store unknown product IDs
        list_of_key_errors = []

        # Read products from CSV into a dictionary
        products_dict = read_dictionary(PRODUCTS_FILE, PRODUCT_ID_INDEX)

        # Process requests and print receipt
        print(STORE_NAME)
        print()

        with open(REQUEST_FILE, "r") as infile:
            reader = csv.reader(infile)
            next(reader) 

            for row in reader:
                product_num = row[PRODUCT_ID_INDEX]
                quantity = int(row[QUANTITY_INDEX])

                try:
                    # Get product info
                    product_info = products_dict[product_num]
                    product_name = product_info[PRODUCT_NAME_INDEX]
                    product_price = product_info[PRODUCT_PRICE_INDEX]

                    # Update subtotal and total quantity
                    subtotal += product_price * quantity
                    total_quantity += quantity

                    # Print each item in receipt
                    print(f"{product_name}: {quantity} @ ${product_price}")

                except KeyError as key_err:
                    # If product ID is unknown, add it to list of key errors
                    list_of_key_errors.append(key_err)

            # Calculating tax_amount and total
            tax_amount = subtotal * SALES_TAX
            total = subtotal + tax_amount

            # Reciept purchase and summary
            print(f"\nTotal Items: {total_quantity}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${tax_amount:.2f}")
            print(f"Total: ${total:.2f}")

            print(f"\nThank you for shopping at {STORE_NAME}!")
            print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
        
    except FileNotFoundError as file_err:
        print(f"Error: missing file\n{file_err}")
    except PermissionError as permiss_err:
        print(f"Error: Permission denied. Please check your file permissions.\n{permiss_err}")
    
    # Print unknown product IDs
    if list_of_key_errors:
        print("\nError: unknown product ID(s) in the request.csv file")
        for key_err in list_of_key_errors:
            print(key_err)
    
def read_dictionary(filename, key_column_index):
    """Reads CSV file and returns a dictionary of products.

    Parameters:
        filename (str): The name of the CSV file.
        key_column_index (int): The index of the column to use as keys in the dictionary.

    Returns:
        dict: A dictionary containing product information.
    """

    product_dict = {}

    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        next(reader)

        for row in reader:
            product_num = row[key_column_index]
            product_name = row[PRODUCT_NAME_INDEX]
            product_price = float(row[PRODUCT_PRICE_INDEX])

            # Store product info in dictionary
            product_dict[product_num] = [product_num, product_name, product_price]

    return product_dict

if __name__ == "__main__":
    main()


# Exceeding the Requirements:
# While this may seem kind of silly my added feature is a more robust error handling system that will 
# list all key_err's in request.csv (if multiple)!
# At first I didn't udnerstand why we wrote our execptions like this except KeyError as key_err: instead of this:

# except FileNotFoundError:
#     print("Error: File not found. Please make sure the file exists.")
# except PermissionError:
#     print("Error: Permission denied. Please check your file permissions.")
# except KeyError:
#     print("Error: Key not found in dictionary. Please check the request file for mistakes.")

# That's when I understood that key_err was variable that held the error when the try block failed
# That allows us to the print that variable along with the message otherwise you would just get the error message
# And not know the what key or file was wrong/missing
# However The problem with:

# except KeyError as key_err:
#         # Handle KeyError exception
#         print(f"Error: unknown product ID in the {REQUEST_FILE} file")
#         print(key_err.args)

# Is that it will only print the first key_err that occured even if there were multiple
# However after I learned as key_err is a variable I could append that vairable to a list after 
# each row iteration allowing me to find allow errors and display them all at the end instead of just one
# The best part is it doesn't mess with the regular flow of the program because the try block only executes
# if an exception isn't raised allowing the program to function properly even if there are errors in the request.csv (So cool!)

# I know this is a small addition but it took me a good chunck of time to figure out!



