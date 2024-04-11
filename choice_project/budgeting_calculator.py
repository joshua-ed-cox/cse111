import csv

# File Path
CATEGORIES_CSV = "categories.csv"


def main():
    categories = read_categories_from_csv(CATEGORIES_CSV)

    # Allocate paycheck amounts to categories and update the CSV file
    track_spending(categories, CATEGORIES_CSV)
    
    # Adjust category amounts based on user spending and update the CSV file
    modify_spending(categories, CATEGORIES_CSV)
    
    # shows the updated current_amount for each category and total to the user
    display_categories(categories)


def read_categories_from_csv(csv_file_path):
    """
    Read expense categories from the CSV file.

    Parameters:
        csv_file_path: The file path to the CSV file.

    Returns:
        list: A list of dictionaries containing category information.
    """
    categories = []

    with open(csv_file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            category = {
                'category': row['category'],
                'percent': float(row['percent']),
                'current_amount': float(row['current_amount']),
                'max_amount': float(row['max_amount'])
            }
            categories.append(category)

    return categories


def track_spending(categories, file_path):
    """Prompts the user to enter their paycheck amount, allocates
    the amount to each category based on the percentage defined
    in the CSV file, and updates the current_amount for each category
    in the CSV file.

    Parameters:
        categories: A list of dictionaries containing category information.
        file_path: The file path of the CSV file.
    """
    paycheck_amount = float(input("\nEnter your paycheck amount: "))
    remaining_amount = paycheck_amount

    # Calculate and allocate amount for each category
    for category_data in categories:
        allocation = paycheck_amount * category_data['percent']
        if allocation > category_data['max_amount'] - category_data['current_amount']:
            allocation = category_data['max_amount'] - category_data['current_amount']
        remaining_amount -= allocation

        # Update current amount for the category
        category_data['current_amount'] += allocation

    # If there's remaining amount, allocate it to another category chosen by the user
    while remaining_amount > 0:
        print(f"\nRemaining amount: ${remaining_amount:.2f}")
        print("Choose a category to allocate the remaining amount:")
        for index, category_data in enumerate(categories, start=1):
            if category_data['current_amount'] < category_data['max_amount']:
                print(f"{index}. {category_data['category']} (${category_data['current_amount']}/{category_data['max_amount']})")
        try:
            choice = int(input("Enter the number of the category: "))
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                if selected_category['current_amount'] < selected_category['max_amount']:
                    remaining_space = selected_category['max_amount'] - selected_category['current_amount']
                    amount_to_allocate = min(remaining_amount, remaining_space)
                    selected_category['current_amount'] += amount_to_allocate
                    remaining_amount -= amount_to_allocate
                else:
                    print("Maximum amount reached for this category. Please choose another category.")
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Update the CSV file
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['category', 'percent', 'current_amount', 'max_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(categories)


def modify_spending(categories, file_path):
    """Allows the user to input their spending for each category,
    updates the current_amount for each category, and writes the
    updated data to the CSV file.

    Parameters:
        categories: A list of dictionaries containing category information.
        file_path: The file path of the CSV file.
    """
    # Prompt user for spending amounts
    print("\nEnter your spending for each category:")
    for category_data in categories:
        valid_input = False
        while not valid_input:
            try:
                spending = float(input(f"Spending for {category_data['category']} (${category_data['current_amount']:.2f}): $"))
                if spending < 0:
                    print("Spending amount cannot be negative. Please enter a valid amount.")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

        # Update current amount for the category
        category_data['current_amount'] -= spending
        if category_data['current_amount'] < 0:
            print(f"Warning: Spending for {category_data['category']} exceeds current balance. "
                  f"Setting current amount to $0.")

    # Write updated data to CSV file
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['category', 'percent', 'current_amount', 'max_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(categories)


def display_categories(categories):
    """Displays the updated category balances and calculates the total amount
    of money across all categories.

    Parameters:
        categories: A list of dictionaries containing category information.
    """
    total_amount = 0

    print("\nUpdated Category Balances:")
    for category_data in categories:
        print(f"{category_data['category']}: ${category_data['current_amount']:.2f} / ${category_data['max_amount']:.2f}")
        total_amount += category_data['current_amount']

    print(f"\nTotal amount across all categories: ${total_amount:.2f}")

if __name__ == "__main__":
    main()

