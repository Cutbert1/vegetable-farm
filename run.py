# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get trade figures input from app users.
    while loop repeatedly run for valid strings, 
    which must contain 13 numbers, separated with commas.
    """
    while True:

        print("Please type in trade data for last open market")
        print("Thirteen numbers separated by commas is expected")
        print("For Example: 1343,1564,2675,3456,1985,6352,1853,5411,3452,1762,3286,1623,1527\n")

        data_str = input("Record data here: ")
    
        trade_data = data_str.split(",")
        

        if verify_data(trade_data):
            print("Data is valid...\n")
            break

    return trade_data

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
        return False


    return True

#def update_trade_worksheet(data):
    """
    Access trade work sheet and add new row anytime new valid list data is entered
    """
    print("Trade worksheet is being updated.....\n")
    trade_worksheet = SHEET.worksheet("trade")
    trade_worksheet.append_row(data)
    print("Trade worksheet successfully updated.\n")

#def update_excess_worksheet(data):
    """
    Access excess work sheet and add new row anytime new valid list data is entered and calculated
    """
    print("Trade worksheet is being updated......\n")
    excess_worksheet = SHEET.worksheet("excess")
    excess_worksheet.append_row(data)
    print("Excess worksheet successfully updated.\n")

def update_worksheet(data, worksheet):
    """
    Receives and update relevant worksheet with data provided
    """
    print(f"{worksheet} worksheet is being updated...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} Worksheet successfully updated.\n")

def calculate_excess_data(trade_row):
    """
    Evaluate trade with harvest, then determine excess for each item
    """
    print("Evaluating excess data....\n")
    harvest = SHEET.worksheet("harvest").get_all_values()
    harvest_row = harvest[-1]

    excess_data = []
    for harvest, trade in zip(harvest_row, trade_row):
        excess = int(harvest) - trade
        excess_data.append(excess)
    
    return excess_data

def get_last_week_trade():
    """
    Assembles columns of data in trade worksheet,
    pulling last 7 entries (one week) for each vegetable 
    then return columns data.
    """
    trade = SHEET.worksheet("trade")

    columns = []
    for ind in range(1, 14):
        column = trade.col_values(ind)
        columns.append(column[-7:])
    
    return columns

def calculate_harvest_data(data):
    """
    Evaluate average harvest for each vegetable type, with addition of 20%
    """
    print("Evaluating harvest data....\n")
    new_harvest_data = []

    for column in data:
        column_int = [int(num) for num in column]
        average = sum(column_int) / 7
        harvest_num = average * 2.2
        new_harvest_data.append(round(harvest_num))

    return new_harvest_data


def main():
    """
    Program functions to run
    """
    data = get_trade_data()
    trade_data = [int(num) for num in data]
    update_worksheet(trade_data, "trade")
    new_excess_data = calculate_excess_data(trade_data)
    update_worksheet(new_excess_data, "excess")
    trade_columns = get_last_week_trade()
    harvest_data = calculate_harvest_data(trade_columns)
    update_worksheet(harvest_data, "harvest")

print("Welcome to Vegetable Farm Data Automation")
main()
