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


emp_number = get_employee_number()
print(emp_number)
