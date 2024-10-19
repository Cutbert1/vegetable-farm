# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
SHEET = GSPREAD_CLIENT.open("vegetable_farm")


def get_trade_data():
    """
    Get trade figures input from app users
    """
    print("Please type in trade data for last open market")
    print("Thirteen numbers separated by commas is expected")
    print("For Example: 1343,1564,2675,3456,1985,6352,1853,5411,3452,1762,3286,1623,1527\n")

    data_str = input("Record data here: ")
    
    trade_data = data_str.split(",")
    verify_data(trade_data)

def verify_data(values):
    """
    All string values converted to integers inside the try. 
    If string values can't be converted to integer raise  ValueError.
    Raise ValueError  if integers are not 13 values exactly.
    """
    try:
        [int(value) for value in values]
        if len(values) != 13:
            raise ValueError(
                f"13 values required but you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, try again please.\n")


get_trade_data()
