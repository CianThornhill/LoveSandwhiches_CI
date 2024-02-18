# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #imports entire gspread library
from google.oauth2.service_account import Credentials #imports credentials class from Google oauth2 library

#lists APIS that the program should access to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') #stores creds.
SCOPED_CREDS = CREDS.with_scopes(SCOPE)                     #Stores scoped creds variable.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)            #Passes Gspread authorize method our Scopes Creds.
SHEET = GSPREAD_CLIENT.open('love_sandwiches')              #Accesses love sandwhiches spread sheet.

def get_sales_data():
    """
    Get sales figures input from user
    """

    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    
    sales_data = data_str.split(",") #Removes commas from the data
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int, 
    or if there arent exactly 6 values.
    """
    #print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e: #the valueerror class contains details of error triggered, then assigning that value error object to the e variable.
        print(f"Invalid data: {e}, please try again.\n")

    #print(values)

get_sales_data()