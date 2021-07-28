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
    print(f"The value is {(input_data).title()}\n")

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


def add_candidate():
    """
    Run all program functions to add a candidate to the
    Redeployment Process and save the data to the redeployment pool
    worksheet
    """
    print("Please proceed to add a new employee.\n")
    emp_number = get_employee_number()
    emp_name = get_input("first name")
    emp_surname = get_input("surname")
    emp_department = get_input("department")
    emp_position = get_input("position")
    employee = [emp_number, emp_name, emp_surname, "emp_age",
                "emp_gender", emp_department, emp_position, "emp_salary",
                "emp_years", "emp_months", "emp_date", " ", "Active"]
    print(employee)


print("Welcome to the capture screen for the Redeployment Process.")
add_candidate()
