import gspread
from google.oauth2.service_account import Credentials
import inquirer
from datetime import datetime
import pandas as pd
import numpy as np


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("redeployment_report")

# The below code is utilised to perform the action of adding a
# new candidate to the redeployment pool.


def get_employee_number():
    """
    Get a six digit employee number from the user.
    Run a while loop for user to input data,
    which must be a string of 6 numbers and it cannot be
    a duplicate employee number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter a six digit employee number.")
        print("The number should not contain any letters or"
              " special characters.")
        print("The number should be a unique value.")
        print("Example: 123456\n")

        employee_number = input("Enter the employee number here:\n")

        if validate_number(employee_number):
            print("Valid employee number captured.\n")
            break

    return employee_number


def validate_number(value):
    """
    Inside the try, converts string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values. The second validation checks
    if the string exists in the employee list from the redeployment pool,
    if it does the user is notified to enter a unique value.
    """
    try:
        int(value)
        if len(value) != 6:
            raise ValueError(
                f"{len(value)} digits"
            )
        employees = retrieve_dataset("redeployment_pool",
                                     "Employee Number")
        if value in employees:
            raise ValueError(f"the duplicate employee number {value}")
    except ValueError as e:
        print(f"Only a unique 6 digit number is accepted, you entered {e},"
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
        print("You cannot enter a number.\n")

        input_data = input(f"Enter the {name} here:\n")

        if validate_data(input_data):
            print(f"Valid {name} captured.\n")
            break

    return input_data.title()


def validate_data(value):
    """
    Inside the try, checks if the string is numeric,
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
        print(f"The {title} should be between the range {range}.\n")

        number = input(f"Enter the {title} here:\n")

        if validate_range(number, range, given_range):
            print(f"Valid {title} captured.\n")
            break

    return number


def validate_range(number, range, given_range):
    """
    Inside the try, converts string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if value is not between the given range.
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
    """
    while True:
        gender = [inquirer.List("gender",
                                message="Please select the "
                                "employee's gender",
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
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter the date of entry / start date")
        print("of the redeployment process for the employee.")
        print("Please enter in the format DD/MM/YYYY.")
        print("Example: 01/07/2021. \n")

        date = input("Enter the start date here:\n")

        if validate_date(date):
            print("Valid date captured.\n")
            break

    return date


def validate_date(my_str_date):
    """
    Raises ValueError if strings cannot be converted into a date and
    if it is in the incorrect format.
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
    Updates the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def add_candidate():
    """
    Run all program functions to add a candidate to the
    Redeployment Process and save the data to the redeployment pool
    worksheet.
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
                " ", " ", " ", "Active"]
    update_sheet(employee, "redeployment_pool")
    sheet = SHEET.worksheet("redeployment_pool")
    cell = sheet.find(emp_number)
    row_no = "%s" % (cell.row)
    cell_2 = sheet.find("Entry Date")
    col_no = "%s" % (cell_2.col)
    sheet.update_cell(row_no, col_no, emp_date)
    main()


def retrieve_dataset(worksheet, heading):
    """
    Utilises pandas to return the worksheet to python
    """
    wks = SHEET.worksheet(worksheet)
    data = wks.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    identifier = df[heading]
    employee_list = identifier.to_list()
    return employee_list


def remove_placed_retrenched_employees():
    employees = retrieve_dataset("redeployment_pool", "Employee Number")
    placed_employees = retrieve_dataset("placed_candidates", "Employee Number")
    retrenched_employees = retrieve_dataset("retrenched_candidates",
                                            "Employee Number")
    return [x for x in employees if x not in placed_employees
            and x not in retrenched_employees]


def retrieve_headers():
    """
    Utilises pandas to return the worksheet to python
    """
    wks = SHEET.worksheet("redeployment_pool")
    data = wks.get_all_values()
    headers = data.pop(0)
    return(headers)


def select_employee():
    """
    Utilise the Employee Number as the identifier to select
    the row of data to update
    """
    choices_list = remove_placed_retrenched_employees()
    while True:
        employee_no = [inquirer.List("employee_number",
                                     message="Please select the "
                                     "employee number to update",
                                     choices=choices_list,), ]
        answers = inquirer.prompt(employee_no)
        print(f"You have selected {answers} \n")
        employee_number = answers["employee_number"]
        break

    return (employee_number)


def select_field():
    """
    Utilise the headers as the identifier to select
    the column of data to update
    """
    headers = retrieve_headers()
    options_list = []
    options_list.extend([headers[1], headers[2], headers[3],
                        headers[4], headers[5], headers[6],
                        headers[7], headers[8], headers[9],
                        headers[10]])
    while True:
        heading_options = [inquirer.List("update_option",
                                         message="Please select the "
                                         "option to update",
                                         choices=options_list,), ]
        answers = inquirer.prompt(heading_options)
        print(f"You have selected {answers} \n")
        break

    return (answers["update_option"])


def update_another_field():
    """
    Checks with the user if they would like to update
    another field. User answers Yes or No
    """
    while True:
        yes_or_no = [inquirer.List("choice",
                                   message="Would you like to "
                                   "return to the update menu?",
                                   choices=["Yes", "No"],), ]
        answers = inquirer.prompt(yes_or_no)
        print(f"You have selected {answers} \n")
        break

    return (answers["choice"])


def update_field():
    """
    Calls the correct function to update the field value
    based on outcome of select_field()
    """
    new_value = 0
    field = select_field()
    age_range = range(18, 76, 1)
    salary_range = range(100, 100001, 1)
    year_range = range(1, 51, 1)
    month_range = range(1, 11, 1)
    if field == "Name":
        first_name = get_input("first name")
        name = "Name", f"{first_name}"
        new_value = name
    elif field == "Surname":
        last_name = get_input("surname")
        surname = "Surname", f"{last_name}"
        new_value = surname
    elif field == "Age":
        how_old = get_number("age", "age", "18 to 75", age_range)
        age = "Age", f"{how_old}"
        new_value = age
    elif field == "Gender":
        assignment = get_gender()
        gender = "Gender", f"{assignment}"
        new_value = gender
    elif field == "Department":
        depo = get_input("department")
        department = "Department", f"{depo}"
        new_value = department
    elif field == "Position":
        job = get_input("position")
        position = "Position", f"{job}"
        new_value = position
    elif field == "Monthly Salary":
        paid = get_number("salary", "salary",
                          "100 to 100 000", salary_range)
        salary = "Monthly Salary", f"{paid}"
        new_value = salary
    elif field == "Tenure -years":
        service_years = get_number("years of service",
                                   "years of service", "1 to 50", year_range)
        years = "Tenure -years", f"{service_years}"
        new_value = years
    elif field == "Tenure -months":
        service_months = get_number("months of service",
                                    "months of service", "1 to 11",
                                    month_range)
        months = "Tenure -months", f"{service_months}"
        new_value = months
    elif field == "Entry Date":
        entry_date = get_date()
        date_one = "Entry Date", f"{entry_date}"
        new_value = date_one
    return new_value


def update_single_cell(emp_value, worksheet, column_value, change_value):

    print(f"Updating {worksheet} worksheet...\n")
    sheet = SHEET.worksheet(worksheet)
    cell = sheet.find(emp_value)
    row_no = "%s" % (cell.row)
    cell_2 = sheet.find(column_value)
    col_no = "%s" % (cell_2.col)
    sheet.update_cell(row_no, col_no, change_value)
    print(f"{worksheet} cell: row{row_no}, col{col_no} successfully"
          f"updated with value: {change_value} \n")


def update_process():
    """
    Calls the functions to use inquirer to select the
    employee number and the datafield that the user
    wishes to update. Calls the function to select/ input
    new value and triggers the update of the worksheet single cell
    """
    emp_value = select_employee()
    field_updated = update_field()
    column_value = field_updated[0]
    change_value = field_updated[1]
    update_single_cell(emp_value, "redeployment_pool",
                       column_value, change_value)


def update_candidate():
    """
    Calls the functions to use inquirer to select the
    employee number and the datafield that the user
    wishes to update
    """
    update_process()
    answer = update_another_field()
    if answer == "Yes":
        update_process()
        update_another_field()
    main()


def fetch_current_salary(worksheet, emp_value, column_value):
    """
    Fetches the current monthly salary of the
    employee to utilise to update the new monthly
    salary and calculate the difference.
    """
    print(f"Fetching current salary from {worksheet}...\n")
    sheet = SHEET.worksheet(worksheet)
    cell = sheet.find(emp_value)
    row_no = "%s" % (cell.row)
    cell_2 = sheet.find(column_value)
    col_no = "%s" % (cell_2.col)
    salary = sheet.cell(row_no, col_no).value
    return salary


def update_exit_date_status(worksheet, worksheet_two, emp_value, status_value):
    """
    Confirms that the employee has been added to the replaced
    worksheet. Updates the exit date and status on the
    redeployment_pool sheet.
    """
    print(f"Fetching employee number from {worksheet}...\n")
    sheet = SHEET.worksheet(worksheet)
    cell = sheet.find(emp_value)
    try:
        print("Updating exit date and status")
        sheet = SHEET.worksheet(worksheet_two)
        cell = sheet.find(emp_value)
        row_no = "%s" % (cell.row)
        cell_2 = sheet.find("Exit Date")
        col_no = "%s" % (cell_2.col)
        today_date = datetime.now().strftime('%d/%m/%Y')
        sheet.update_cell(row_no, col_no, today_date)
        print(f"{worksheet_two} cell: row{row_no}, col{col_no} successfully"
              f"updated with value: {today_date} \n")
        days_in_pool("redeployment_pool", emp_value)
        cell_3 = sheet.find("Status")
        col_2_no = "%s" % (cell_3.col)
        status_value = status_value
        sheet.update_cell(row_no, col_2_no, status_value)
        print(f"{worksheet_two} cell: row{row_no}, col{col_2_no} successfully"
              f"updated with value: {status_value} \n")
    except ValueError as e:
        print(f" A ValueError has occurred: {e}")
        print("Please repeat the place employee process./n")


def days_in_pool(worksheet, emp_value):
    from datetime import date

    print("Calculating days in pool...\n")
    sheet = SHEET.worksheet(worksheet)
    cell = sheet.find(emp_value)
    row_no = "%s" % (cell.row)
    cell_2 = sheet.find("Entry Date")
    col_no = "%s" % (cell_2.col)
    entry_date = (sheet.cell(row_no, col_no).value).split("/")
    entry_year = int(entry_date[2])
    entry_month = int(entry_date[1])
    entry_day = int(entry_date[0])
    cell_3 = sheet.find("Exit Date")
    col_2_no = "%s" % (cell_3.col)
    exit_date = (sheet.cell(row_no, col_2_no).value).split("/")
    exit_year = int(exit_date[2])
    exit_month = int(exit_date[1])
    exit_day = int(exit_date[0])
    d0 = date(entry_year, entry_month, entry_day)
    d1 = date(exit_year, exit_month, exit_day)
    days_in_pool = d1 - d0
    days = str(days_in_pool)
    days_no = (days[0] + days[1])
    cell_4 = sheet.find("Days within Pool")
    col_3_no = "%s" % (cell_4.col)
    sheet.update_cell(row_no, col_3_no, int(days_no))
    print(f"{worksheet} cell: row{row_no}, col{col_3_no} successfully"
          f"updated with value: {days_no} \n")


def place_candidate():
    """
    Calls the functions required to select the employee
    number and checks with the user if the new position includes
    a decrease in salary, an increase in salary or if the salary
    remains the same. Calls the function to capture the new salary
    dependent on the selection.
    """
    print("You have chosen to place an employee.")
    emp_value = select_employee()
    print("Has there been a change in monthly salary?/n")

    while True:
        change_in_salary = [inquirer.List("salary_change",
                                          message="Please select the "
                                          "relevant option",
                                          choices=["Decrease",
                                                   "Remains the Same",
                                                   "Increase"],), ]
        answers = inquirer.prompt(change_in_salary)
        print(f"You have selected {answers} \n")
        break
    salary_update = (answers["salary_change"])
    department_position = choose_department_position()
    department = department_position[0]
    position = department_position[1]
    current_salary = int(fetch_current_salary("redeployment_pool", emp_value,
                                              "Monthly Salary"))
    if salary_update == "Decrease":
        salary_range = range(100, (current_salary - 1), 1)
        range_value = f"100 to {current_salary - 1}."
        print(f"The current employee salary is: {current_salary}."
              " Please capture the new decreased salary.")
        paid = get_number("salary", "salary",
                          range_value, salary_range)
        print(f"The new salary has been captured as {paid}.")
        print("Calculating difference in salary")
        difference = (int(paid) - current_salary)
        status = ("Decreased")
    elif salary_update == "Remains the Same":
        print(f"The current employee salary is: {current_salary}."
              " This will remain the same.")
        paid = current_salary
        difference = 0
        status = ("Equal")
    elif salary_update == "Increase":
        salary_range = range((current_salary + 1), 100000, 1)
        range_value = f"{current_salary + 1} to 100000."
        print(f"The current employee salary is: {current_salary}."
              " Please capture the new increased salary.")
        paid = get_number("salary", "salary",
                          range_value, salary_range)
        print(f"The new salary has been captured as {paid}.")
        print("Calculating difference in salary")
        difference = (int(paid) - current_salary)
        status = ("Increased")
    print("Thank you for capturing the placement.")
    placed_employee = [int(emp_value), department, position,
                       int(current_salary), int(paid), int(difference), status]

    update_sheet(placed_employee, "placed_candidates")
    update_exit_date_status("placed_candidates",
                            "redeployment_pool", emp_value, "Placed")
    main()


def choose_department_position():
    """
    Choose the new department and the new position of the employee.
    """
    print("Please enter the New Department in which the"
          " employee has been placed.")
    depo = get_input("department")
    print(f"The New Department has been set as {depo}. \n")
    print("Please enter the New Position in which the"
          " employee has been placed.")
    job = get_input("position")
    print(f"The New Position has been set as {job}. \n")
    return (depo, job)


def retrench_employee():
    """
    Calls the functions required to retrench an employee. Calculates the
    retrenchment package. Add the new data  to the spreadsheet.
    """
    print("You have chosen to retrench an employee.")
    emp_value = select_employee()
    print("Calculating retrenchment package...\n")
    print("Fetching salary...\n")
    sheet = SHEET.worksheet("redeployment_pool")
    cell = sheet.find(emp_value)
    row_no = "%s" % (cell.row)
    cell_2 = sheet.find("Monthly Salary")
    col_no = "%s" % (cell_2.col)
    salary_current = (sheet.cell(row_no, col_no).value)
    print("Fetching Tenure -years...\n")
    sheet = SHEET.worksheet("redeployment_pool")
    cell_3 = sheet.find("Tenure -years")
    col_2_no = "%s" % (cell_3.col)
    tenure_years = (sheet.cell(row_no, col_2_no).value)
    print("Fetching Tenure -months...\n")
    sheet = SHEET.worksheet("redeployment_pool")
    cell_4 = sheet.find("Tenure -months")
    col_3_no = "%s" % (cell_4.col)
    tenure_months = (sheet.cell(row_no, col_3_no).value)
    package = ((int(salary_current) * int(tenure_years)) +
               (int(tenure_months) // 12 * int(salary_current)))
    print(f"Retrenchment package calculated as {package}.\n")
    retrenched_employee = [emp_value, package]
    update_sheet(retrenched_employee, "retrenched_candidates")
    update_exit_date_status("retrenched_candidates",
                            "redeployment_pool", emp_value, "Retrenched")
    main()


def display_redeployment_pool():
    wks = SHEET.worksheet("redeployment_pool")
    data = wks.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df.style
    render()


def main():
    """
    Utilises inquirer to provide the user a list of
    actions to perform. Calls the relevant function
    based on the action selected.
    """
    while True:
        questions = [inquirer.List("options",
                     message="Please select an action",
                                   choices=["Add a new candidate",
                                            "Update candidate details",
                                            "Place a candidate", "Retrench"
                                            " a candidate",
                                            "Exit the process", "Test"],), ]
        answers = inquirer.prompt(questions)
        break
    selection = answers["options"]
    if selection == "Add a new candidate":
        return add_candidate()
    elif selection == "Update candidate details":
        return update_candidate()
    elif selection == "Place a candidate":
        return place_candidate()
    elif selection == "Retrench a candidate":
        return retrench_employee()
    elif selection == "Exit the process":
        print("Thank you for your time.")
    elif selection == "Test":
        display_redeployment_pool()


print("Welcome to the capture screen for the Redeployment Process.")
main()
