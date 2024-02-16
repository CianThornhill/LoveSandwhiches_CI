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
    print(f"The data provided is {data_str}")

get_sales_data()