import gspread
from google.oauth2.service_account import Credentials
import inquirer
from datetime import datetime
import pandas as pd
import xlrd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("redeployment_report")


def get_employee_number():
    """
    Get a six digit employee number from the user.
    Run a while loop for user to input data,
    which must be a string of 6 numbers.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter a six digit employee number.")
        print("The number should not contain any letters or"
              " special characters.")
        print("Example: 123456\n")

        employee_number = input("Enter the employee number here:\n")

        if validate_number(employee_number):
            print("Employee Number captured\n")
            break

    return employee_number


def validate_number(value):
    """
    Inside the try, converts string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        int(value)
        if len(value) != 6:
            raise ValueError(
                f"{len(value)}"
            )
    except ValueError as e:
        print(f"Only a 6 digit number is accepted, you entered {e},"
              " please try again.\n")
        return False

    return True


def get_input(name):
    """
    Get the data input from the user.
    Run a while loop for user to input data,
    which must not contain numbers.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print(f"Please enter the {name} of the employee.")
        print("You cannot enter a number.")

        input_data = input(f"Enter the {name} here:\n")

        if validate_data(input_data):
            print(f"Valid {name} captured\n")
            break

    return input_data.title()


def validate_data(value):
    """
    Inside the try, checks of the string is numeric,
    Raises ValueError if strings is numeric.
    """
    try:
        if value.isnumeric() is True:
            raise ValueError(f"{value}")
    except ValueError as e:
        print(f"Numbers are not accepted, you entered {e},"
              " please try again.\n")
        return False

    return True


def get_number(title, number, range, given_range):
    """
    Get the input data of the employee from the user.
    Run a while loop for user to input data,
    which must be within the given range.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print(f"Please enter the {title} of the employee.")
        print(f"The {title} should be between the range {range}")

        number = input(f"Enter the {title} here:\n")

        if validate_range(number, range, given_range):
            print(f"Data {title} captured\n")
            break

    return number


def validate_range(number, range, given_range):
    """
    Inside the try, converts string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if value is not between the given range
    """
    try:
        given_range
        number = int(number)
        if number not in given_range:
            raise ValueError(
                f"{number}"
            )
    except ValueError as e:
        print(f"Only a value between {range} is accepted, you entered {e},"
              " please try again.\n")
        return False

    return True


def get_gender():
    """
    Get the gender of the employee from the user.
    Run a while loop for user to select data,
    which must be one of the given values.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        gender = [inquirer.List("gender",
                                message="Please select the "
                                "employee's gender :",
                                choices=["male", "female", "unknown", ],), ]
        answers = inquirer.prompt(gender)
        print("Valid gender selected \n")
        break

    return (answers["gender"])


def get_date():
    """
    Get the entry date of the employee into the
    redeployment process from the user.
    Run a while loop for user to input data,
    which must be a string of letters.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter the date of entry / start date")
        print("of the redeployment process for the employee.")
        print("Please enter in the format DD/MM/YYYY")
        print("Example: 01/07/2021 \n")

        date = input("Enter the start date here:\n")

        if validate_date(date):
            print("Date captured\n")
            break

    return date


def validate_date(my_str_date):
    """
    Raises ValueError if strings cannot be converted into a date and
    if it is in the incorrect format
    """
    try:
        if datetime.strptime(my_str_date, "%d/%m/%Y"):
            return datetime.strptime(my_str_date, "%d/%m/%Y")
        else:
            raise ValueError(f"{my_str_date}")
    except ValueError as e:
        print(f"Incorrect data format,"
              f" should be DD/MM/YYYY, you entered {e} ,"
              " please try again.\n")
        return False

    return True


def update_sheet(data, worksheet):
    """
    Receives a list of values to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def add_candidate():
    """
    Run all program functions to add a candidate to the
    Redeployment Process and save the data to the redeployment pool
    worksheet
    """
    print("Please proceed to add a new employee.\n")
    age_range = range(18, 76, 1)
    salary_range = range(100, 100001, 1)
    year_range = range(1, 51, 1)
    month_range = range(1, 11, 1)
    emp_number = get_employee_number()
    emp_name = get_input("first name")
    emp_surname = get_input("surname")
    emp_age = get_number("age", "age", "18 to 75", age_range)
    emp_gender = get_gender()
    emp_department = get_input("department")
    emp_position = get_input("position")
    emp_salary = get_number("salary", "salary", "100 to 100 000", salary_range)
    emp_years = get_number("years of service", "years of service",
                           "1 to 50", year_range)
    emp_months = get_number("months of service", "months of service",
                            "1 to 11", month_range)
    emp_date = get_date()
    employee = [int(emp_number), emp_name, emp_surname, int(emp_age),
                emp_gender, emp_department, emp_position, int(emp_salary),
                int(emp_years), int(emp_months),
                (emp_date), " ", " ", " ", "Active"]

    update_sheet(employee, "redeployment_pool")


def main():
    questions = [inquirer.List("options",
                 message="Please select the action"
                 " you would like to perform:",
                               choices=["Add a new candidate",
                                        "Update candidate details",
                                        "Place a candidate", "Retrench"
                                        " a candidate"], ), ]
    answers = inquirer.prompt(questions)
    print("Thank you for your selection.")
    options = answers["options"]
    if options == "Add a new candidate":
        add_candidate()


print("Welcome to the capture screen for the Redeployment Process.")
main()
