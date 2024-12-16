## Deleted the previous codes, hence starting afresh in same workspace and repository"
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("vegetable_farm_sales")

VEGETABLES = {
    "1": {"name": "Cabbage", "price": 1.25},
    "2": {"name": "Carrot", "price": 1.50},
    "3": {"name": "Mushroom", "price": 2.00},
    "4": {"name": "Broccoli", "price": 2.50},
    "5": {"name": "Cauliflower", "price": 1.25},
    "6": {"name": "Avocado", "price": 3.50},
    "7": {"name": "Asparagus", "price": 2.00},
    "8": {"name": "Aubergine", "price": 1.00},
    "9": {"name": "Tomato", "price": 1.25},
    "10": {"name": "Cucumber", "price": 1.50},
    "11": {"name": "Spinach", "price": 2.00},
    "12": {"name": "Parsnip", "price": 1.00},
    "13": {"name": "Onion", "price": 1.00},
}

def execute_vegetable_sales():
    """
    Execute vegetable sales
    """
    # Display available items and prices
    print("Welcome to the Vegetable Sales!")
    print("Please select an item:")
 
    for key, vegetable in VEGETABLES.items():
        print(f"{key}. {vegetable['name']} - ${vegetable['price']}")
    
    # Prompt user input
    user_selection = input("Enter the item number you wish to purchase: ")
    
    # Confirm availability of selected item
    if user_selection in VEGETABLES:
        chosen_vegetable = VEGETABLES[user_selection]
        print(f"You have selected {chosen_vegetable['name']}.")
        total_due = chosen_vegetable['price']
        
        # Prompt user payment
        while total_due > 0:
            try:
                user_payment = float(input(f"Please insert ${total_due:.2f} or pay with card: "))
                if user_payment >= total_due:
                    change_returned = user_payment - total_due
                    print(f"Thank you for your purchase! Your change is ${change_returned:.2f}.")
                    break
                else:
                    print("Insufficient payment. Please insert more money.")
                    total_due -= user_payment
            except ValueError:
                print("Invalid payment amount. Please enter a valid number.")
    else:
        print("Invalid selection. Please try again.")
    
    return chosen_vegetable, total_due

def main():
    """
    Run program functions
    """
    vegetable, total_due = execute_vegetable_sales()

main()
