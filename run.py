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
SPREADSHEET = GSPREAD_CLIENT.open("vegetable_farm_sales")
 
VEGETABLES_BOX = {
    "1": {"name": "Cabbage", "price": 37.50},
    "2": {"name": "Carrot", "price": 25.50},
    "3": {"name": "Mushroom", "price": 12.00},
    "4": {"name": "Broccoli", "price": 8.50},
    "5": {"name": "Cauliflower", "price": 15.99},
    "6": {"name": "Avocado", "price": 32.50},
    "7": {"name": "Asparagus", "price": 29.99},
    "8": {"name": "Aubergine", "price": 45.70},
    "9": {"name": "Tomato", "price": 37.99},
    "10": {"name": "Cucumber", "price": 46.50},
    "11": {"name": "Spinach", "price": 26.00},
    "12": {"name": "Parsnip", "price": 33.00},
    "13": {"name": "Onion", "price": 48.99},
}
 
def execute_vegetable_sales():
    """
    Execute vegetable sales
    """
    # Display available produce and prices
    print("Welcome to the Produce Sales!")
    print("Please select an item:")
 
    for key, vegetable in VEGETABLES_BOX.items():
        print(f"{key}. {vegetable['name']} - £{vegetable['price']}")
 
    # Prompt user selection
    while True:
        user_selection = input("Enter the item number you wish to purchase (or type 'exit' to end): ")
 
        if user_selection.lower() == 'exit':
            print("Thank you for checking our produce!")
            return None, 0, False  
 
        # Confirm availability of selected item
        if user_selection in VEGETABLES_BOX:
            chosen_vegetable = VEGETABLES_BOX[user_selection]
            print(f"You have selected {chosen_vegetable['name']}.")
            total_due = chosen_vegetable['price']
 
            # Prompt user payment
            while total_due > 0:
                try:
                    user_payment = float(input(f"Please insert £{total_due:.2f} or pay with card: "))
                    if user_payment >= total_due:
                        change_returned = user_payment - total_due
                        print(f"Thank you for your purchase! Your change is £{change_returned:.2f}.")                       
                        return chosen_vegetable, total_due, True  
                    else:
                        print("Insufficient payment. Please insert more money.")
                        total_due -= user_payment
                except ValueError:
                    print("Invalid payment amount. Please enter a correct amount.")
            break
        else:
            print("Invalid selection. Please try again.")
 
    return None, 0, False  
 
 
def updateworksheet_sales(item: "vegetable", total_due: float):
    """
    Update worksheet for each purchase for back office inventory
    Parameters:
        - item: str
            The name of the item purchased.
        - total_due: float or integer
            The value of the purchase.
 
        Raises:
        - Exception:
            If there is an issue updating the sales worksheet.
    """
    print("Sales worksheet is being updated\n")
    try:
        worksheet = SPREADSHEET.worksheet("sales")
        next_row = len(worksheet.get_all_values()) + 1
 
        worksheet.update_cell(next_row, 1, item["name"])
        worksheet.update_cell(next_row, 2, total_due)
 
    except Exception as e:
        raise Exception(f"An error occurred while updating the sales worksheet: {e}")
    print("Sales Worksheet successfully updated\n")
 
 
def convert_and_sum(all_col_values_except_first):
    """
    Back office to calculate total daily sales at the end of each market day.
    Convert list strings pulled from sales worksheet to 
    float and integer and sum up the daily total
    parameter:
        - all_col_values_except_first: Amount column from worksheet
                                       Excluding the header
    """
 
    for value in all_col_values_except_first:
 
        try:
            float(value)
        except ValueError:
            raise ValueError(f"Invalid data '{value}': All data must be integer or float string.")
 
    float_values = [float(value) for value in all_col_values_except_first]
 
    total_sum = sum(float_values)
    print(f"Total daily Sales: £{total_sum}")
 
    return total_sum
 

def calculate_daily_sales():
    """
    Back office to calculate daily sales at the end of each market day.
    Pull list of strings from sales worksheet
    """
    worksheet = SPREADSHEET.worksheet("sales")
    colvalues = worksheet.col_values(2)  
    all_col_values_except_first = colvalues[1:]   
 
    return all_col_values_except_first
 
 
def main():
    """
    Run program functions
    """
    vegetable, total_due, should_record = execute_vegetable_sales()
    if should_record:
        updateworksheet_sales(vegetable, total_due)
    total_sum = calculate_daily_sales()
    convert_and_sum(total_sum)
 
main()