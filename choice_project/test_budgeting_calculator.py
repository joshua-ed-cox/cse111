import pytest
import csv
from budgeting_calculator import read_categories_from_csv, track_spending, modify_spending

# file path
CATEGORIES_CSV = "test_categories.csv"

@pytest.fixture
def categories():
    # Hardcoded sample data
    return [
        {'category': 'Rent', 'percent': 0.2, 'current_amount': 500, 'max_amount': 2000},
        {'category': 'Groceries', 'percent': 0.1, 'current_amount': 100, 'max_amount': 500},
        {'category': 'Utilities', 'percent': 0.15, 'current_amount': 200, 'max_amount': 1000}
    ]

def test_read_categories_from_csv(categories):
    # Define a sample CSV file string
    csv_content = """category,percent,current_amount,max_amount
Rent,0.2,500,2000
Groceries,0.1,100,500
Utilities,0.15,200,1000"""

    with open('test_categories.csv', 'w') as f:
        f.write(csv_content)

    result = read_categories_from_csv('test_categories.csv')

    assert result == categories

def test_track_spending(categories):

    with pytest.raises(OSError):
        track_spending(categories, CATEGORIES_CSV)

    # Write the modified categories list back to the CSV file
    write_categories_to_csv(categories, CATEGORIES_CSV)

    # Read the categories from the CSV file again
    updated_categories = read_categories_from_csv(CATEGORIES_CSV)

    assert updated_categories[0]['current_amount'] == 900
    assert updated_categories[1]['current_amount'] == 300
    assert updated_categories[2]['current_amount'] == 500

def test_modify_spending(categories):

    
    with pytest.raises(OSError):
        modify_spending(categories, CATEGORIES_CSV)

    # Write the modified categories list back to the CSV file
    write_categories_to_csv(categories, CATEGORIES_CSV)

    # Read the categories from the CSV file again
    updated_categories = read_categories_from_csv(CATEGORIES_CSV)

    assert updated_categories[0]['current_amount'] == 450
    assert updated_categories[1]['current_amount'] == 20
    assert updated_categories[2]['current_amount'] == 80

def write_categories_to_csv(categories, file_path):
    """Writes the categories list to the CSV file.

    Parameters:
        categories (list): A list of dictionaries containing category information.
        file_path (str): The file path of the CSV file.
    """
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['category', 'percent', 'current_amount', 'max_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(categories)

pytest.main(["-v", "--tb=line", "-rN", __file__])