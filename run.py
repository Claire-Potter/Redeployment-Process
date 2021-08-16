# Import additional libraries to utilise functionality.
import gspread
from google.oauth2.service_account import Credentials
from InquirerPy import inquirer, prompt
import inquirer
from datetime import datetime
import pandas as pd
from IPython.display import display
from prompt_toolkit import __version__ as ptk_version

PTK3 = ptk_version.startswith('3.')

# Setup the scope and credentials for
# accessing google sheets. This was created as per the
# Code Institute Love Sandwiches project.

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
    Returns:
        string. The six digit number in string format.
    References:
        This function was created based on the get_sales_data() function
        created in the Code Institute Love Sandwiches project. It has been
        adjusted to align with this application's requirements.
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
    Args:
        value - string entered by the user.
    Returns:
        True, the input is valid or False, the input is not valid.
    Raises:
        ValueError if string cannot be converted into int,
        or if there aren't exactly 6 values. The second validation checks
        if the string exists in the employee list from the redeployment pool,
        if it does the user is notified to enter a unique value.
    References:
        This function was created based on the validate_data(values) function
        created in the Code Institute Love Sandwiches project. It has been
        adjusted to align with this application's requirements.
    """
    try:
        int(value)
        if len(value) != 6:
            raise ValueError(
                f"{len(value)} digits"
            )
        employees = retrieve_dataset("redeployment_pool",
                                     [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
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
    Args:
        name - string which must not contain numeric values.
    Returns:
        string with first letter/s converted to uppercase.
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
    Inside the try, checks if the string is numeric.
    Args:
        value - string captured by user.
    Returns:
        True, the input is valid or False, the input is not valid.
    Raises:
        ValueError if strings is numeric.

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
    Args:
        title - string, number - string, range - string,
        given_range - the relevant number range.
    Returns:
        integer. The captured string converted to an integer.
    """
    while True:
        print(f"Please enter the {title} of the employee.")
        print(f"The {title} should be between the range {range}.\n")

        number = input(f"Enter the {title} here:\n")

        if validate_range(number, range, given_range):
            print(f"Valid {title} captured.\n")
            break

    return int(number)


def validate_range(number, range, given_range):
    """
    Inside the try, converts string value into integer.
    Args:
        number - string, range - string,
        given_range - the relevant number range.
    Raises:
        ValueError if strings cannot be converted into int,
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
    Returns:
        string - gender selection.
    """
    while True:
        gender = [{"type": "list",
                   "message": "Please select the employee's gender",
                   "choices": ["male", "female", "unknown"], }, ]
        result = prompt(gender)
        name = result[0]
        print("Valid gender selected \n")
        print(name)
        break

    return (name)


def get_date():
    """
    Get the entry date of the employee into the
    redeployment process from the user.
    Run a while loop for user to input data,
    The loop will repeatedly request data, until it is valid.
    Returns:
        date - string
    """
    while True:
        print("Please enter the date of entry / start date")
        print("of the redeployment process for the employee.")
        print("The date should occur before today's date.")
        print("Please enter in the format DD/MM/YYYY.")
        print("Example: 01/07/2021. \n")

        date = input("Enter the start date here:\n")

        if validate_date(date):
            print("Valid date captured.\n")
            break

    return date


def validate_date(my_str_date):
    """
    Validates the format of the input as a date.
    Args:
        my_str_date - string captured by user
    Returns:
        True, the input is valid or False, the input is not valid.
    Raises:
        ValueError if string cannot be converted into a date and
        if it is in the incorrect format.
        ValueError if the captured_date is greater than or equal to
        today's date.
    References:
        The following article was refernced to convert to date:
        https://stackoverflow.com/questions/52260789/update-googlesheet-cell-with-timestamp-from-python
    """
    try:
        captured_date = datetime.strptime(my_str_date, "%d/%m/%Y")
        if captured_date.date() >= datetime.today().date():
            raise ValueError(f"{my_str_date} which is equal to"
                             " or occurs after today.")
        elif datetime.strptime(my_str_date, "%d/%m/%Y"):
            return datetime.strptime(my_str_date, "%d/%m/%Y")
        else:
            raise ValueError(f"{my_str_date}")
    except ValueError as e:
        print(f"The date format should be DD/MM/YYYY"
              f" and it should occur before today's date, you entered {e} ,"
              " please try again.\n")
        return False

    return True


def update_sheet(data, worksheet):
    """
    Receives a list of values to be inserted into a worksheet
    Updates the relevant worksheet with the data provided.
    Args:
        data - list of user input, worksheet -string name of worksheet
    References:
        This function was created based on the update_worksheet()
        function created in the Code Institute Love Sandwiches project.
        It has been adjusted to align with this application's requirements.
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
    References:
    The following article was referenced to return a cell's address:
    https://github.com/burnash/gspread/issues/41
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
    employee = [emp_number, emp_name, emp_surname, emp_age,
                emp_gender, emp_department, emp_position, emp_salary,
                emp_years, emp_months,
                " ", " ", " ", "Active"]
    update_sheet(employee, "redeployment_pool")
    sheet = SHEET.worksheet("redeployment_pool")
    cell = sheet.find(emp_number)
    row_no = "%s" % (cell.row)
    cell_2 = sheet.find("Entry Date")
    col_no = "%s" % (cell_2.col)
    sheet.update_cell(row_no, col_no, emp_date)
    main()


# The below functions are used to select an employee and update data.


def retrieve_dataset(worksheet, columns_list):
    """
    Utilises pandas to return the worksheet to python.
    The employee list is utilised by the user to select
    an employee.
    Args:
        worksheet - string name of worksheet, columns_list -
        list of columns to omit
    Returns:
        columns combined and converted to a list of strings
    """
    wks = SHEET.worksheet(worksheet)
    data = wks.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df = df.loc[df["Status"] != "Placed"]
    df = df.loc[df["Status"] != "Retrenched"]
    df = df.drop(df.columns[columns_list], axis=1)
    df["combined"] = df.values.tolist()
    employees = df["combined"].tolist()
    emp_list = list(map(" ".join, employees))
    return emp_list


def retrieve_headers():
    """
    Utilises pandas to return the worksheet to python.
    The headers are retrieved to create a picklist of
    fields the user can choose to update.
    Returns:
        list of column headers
    """
    wks = SHEET.worksheet("redeployment_pool")
    data = wks.get_all_values()
    headers = data.pop(0)
    return(headers)


def select_employee():
    """
    Utilise the Employee Number, Name and Surname as the identifier to select
    the row of data to update. Utilises inquirer functionality to
    create and format the list.
    Returns:
        the employee number as a string.
    """
    choices_list = retrieve_dataset("redeployment_pool", [3, 4, 5, 6, 7,
                                    8, 9, 10, 11, 12, 13])
    while True:
        employee = [inquirer.List("employee",
                                  message="Please select the "
                                  "employee to update",
                                  choices=choices_list,), ]
        answers = inquirer.prompt(employee)
        print(f"You have selected {answers} \n")
        employee = answers["employee"]
        emp_values = employee.split()
        emp_value = emp_values[0]
        break

    return (emp_value)


def select_field():
    """
    Utilise the headers as the identifier to select
    the column of data to update. Utilises inquirer functionality to
    create and format the list.
    Returns:
        the selected header as a string.
    References:
        the list.extend function was used as per
        the stackoverflow post:
        https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python/20196202
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
    Returns:
        answer as a string
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
    Uses if/elif/else to call the correct function to update the field value
    based on outcome of select_field()
    Returns:
        tuple - new_value which is utilised to select
        the column by the header value and to provide
        the change_value, which is the input captured by the user.
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
    """
    Uses the employee number and the header to find the correct
    cell in the spreadsheet to update. Overwrites with the new
    value provided by the user.
    Args:
        emp_value - string employee number, worksheet - string worksheet name,
        column_value - string column header, change_value -
        string captured by user.
    References:
        the following article was referenced
        to update a single cell value:
        https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell
        The following article was referenced to return a cell's address:
        https://github.com/burnash/gspread/issues/41
    """
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
    employee and the datafield that the user
    wishes to update. Calls the function to select/ input
    new value and triggers the update of the worksheet single cell.
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
    employee and the datafield that the user
    wishes to update.
    """
    update_process()
    answer = update_another_field()
    if answer == "Yes":
        update_process()
        update_another_field()
    main()


# The below functions are used to place an employee into
# a new position and add them to the placed employees sheet


def fetch_current_salary(worksheet, emp_value, column_value):
    """
    Fetches the current monthly salary of the
    employee to utilise to update the new monthly
    salary and calculate the difference.
    Args:
        worksheet - string name of worksheet,
        emp_value - string employee number,
        column_value - string name of column.
    Returns:
        integer salary value
    References:
        the following article was referenced to
        locate data using cell coordinates:
        https://www.makeuseof.com/tag/read-write-google-sheets-python/
        The following article was referenced to return a cell's address:
        https://github.com/burnash/gspread/issues/41
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
    Confirms that the employee has been added to the placed
    worksheet. Updates the exit date and status on the
    redeployment_pool sheet.
    Args:
        worksheet - string name of worksheet,
        worksheet_two - string name of second worksheet,
        emp_value - string employee number,
        status_value - string value of status column.
    Raises:
        Value Error as e if an error occurs in updating the values in the
        worksheet.
    References:
        the following article was referenced
        to update a single cell value:
        https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell4
        The following article was referenced to return a cell's address:
        https://github.com/burnash/gspread/issues/41
        The following article was refernced to convert to date:
        https://stackoverflow.com/questions/52260789/update-googlesheet-cell-with-timestamp-from-python
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
        today_date = datetime.now().strftime("%d/%m/%Y")
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
        print("Please repeat the place employee process.\n")


def days_in_pool(worksheet, emp_value):
    """
    Retrieves the entry date and exit date from the redeployment pool
    sheet and splits the values into year, month and day.
    Calculates the days within the pool and adds it back to the sheet.
    Args:
        worksheet - string name of worksheet,
        emp_value - string employee number.
    References:
        the following article was referenced
        to update a single cell value:
        https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell
        The following article was referenced to
        locate data using cell coordinates:
        https://www.makeuseof.com/tag/read-write-google-sheets-python/
        The following article was referenced to return a cell's address:
        https://github.com/burnash/gspread/issues/41
        The following article was referenced for the days in pool calculation:
        https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
        The following article was referenced to split the string:
        https://stackoverflow.com/questions/7844118/how-to-convert-comma-delimited-string-to-list-in-python
    """
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
    dependent on the selection. Adds the updates to the redeployment
    pool worksheet and the employee to the placed employees worksheet.
    References:
        to access specific cell and return the value
        from the dataframe:
        https://pythonhow.com/accessing-dataframe-columns-rows-and-cells/
    """
    print("You have chosen to place an employee.")
    emp_value = select_employee()
    sheet = SHEET.worksheet("redeployment_pool")
    data = sheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df2 = df.set_index("Employee Number", drop=False)
    name = df2.loc[emp_value, "Name"]
    surname = df2.loc[emp_value, "Surname"]
    print("Has there been a change in monthly salary?\n")

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
        difference = (paid - current_salary)
        status = ("Increased")
    print("Thank you for capturing the placement.")
    placed_employee = [emp_value, name, surname, department, position,
                       current_salary, paid, difference, status]

    update_sheet(placed_employee, "placed_employees")
    update_exit_date_status("placed_employees",
                            "redeployment_pool", emp_value, "Placed")
    main()


def choose_department_position():
    """
    Choose the new department and the new position of the employee.
    Returns:
       the string values for new department and new position.
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


# The below function is utilised to retrench an employee


def retrench_employee():
    """
    Calls the functions required to retrench an employee. Calculates the
    retrenchment package. Adds the new data  to the spreadsheet.
    References:
        to access specific cell and return the value
        from the dataframe:
        https://pythonhow.com/accessing-dataframe-columns-rows-and-cells/
        The following article was referenced to locate data
        using cell coordinates:
        https://www.makeuseof.com/tag/read-write-google-sheets-python/
        The following article was referenced to return a cell's address:
        https://github.com/burnash/gspread/issues/41
    """
    print("You have chosen to retrench an employee.")
    emp_value = select_employee()
    sheet = SHEET.worksheet("redeployment_pool")
    data = sheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df2 = df.set_index("Employee Number", drop=False)
    name = df2.loc[emp_value, "Name"]
    surname = df2.loc[emp_value, "Surname"]
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
    retrenched_employee = [emp_value, name, surname, package]
    update_sheet(retrenched_employee, "retrenched_employees")
    update_exit_date_status("retrenched_employees",
                            "redeployment_pool", emp_value, "Retrenched")
    main()


# The below functions are utilised to fetch the worksheets,
# and setup the dataframe display to display the data tables in
# the console.


def display_remove_rows(worksheet, sort_by, columns_list):
    """
    Fetches the worksheet from google sheets. Returns all
    data and creates headers as columns. Sorts the data, and
    drops unwanted columns. Removes rows of employees who's
    status is Active. Removes the index from the display.
    Args:
         worksheet - string name of worksheet,
         sort_by - string column name to sort data by,
         columns_list - list of columns to be dropped.
    References:
        The following article was referenced to create the .loc
        code:
        https://re-thought.com/how-to-change-or-update-a-cell-value-in-python-pandas-dataframe/
        The following article was referenced for dataframe formatting:
        https://mode.com/example-gallery/python_dataframe_styling/
        The following article was referenced to hide columns and index:
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.hide_columns.html#pandas.io.formats.style.Styler.hide_columns
    """
    wks = SHEET.worksheet(worksheet)
    data = wks.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df = df.sort_values(by=sort_by)
    df = df.drop(df.columns[columns_list], axis=1)
    df = df.loc[df["Status"] != "Active"]
    display((df.to_string(index=False)))


def display_redeployment_pool(worksheet, sort_by, columns_list):
    """
    Fetches the worksheet from google sheets. Returns all
    data and creates headers as columns. Sorts the data, and
    drops unwanted columns. Removes the index from the display.
    Args:
         worksheet - string name of worksheet,
         sort_by - string column name to sort data by,
         columns_list - list of columns to be dropped.
    References:
        The following article was referenced for dataframe formatting:
        https://mode.com/example-gallery/python_dataframe_styling/
        The following article was referenced to hide columns and index:
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.hide_columns.html#pandas.io.formats.style.Styler.hide_columns
    """
    wks = SHEET.worksheet(worksheet)
    data = wks.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    df = df.sort_values(by=sort_by)
    df = df.drop(df.columns[columns_list], axis=1)
    display((df.to_string(index=False)))


def summary_report():
    """
    Calls the function to fetch the data. Displays the
    redeployment pool summary table.
    """
    print("The below table displays the employees")
    print("added to the redeployment pool.")
    print("It has been sorted according to status.\n")

    display_redeployment_pool("redeployment_pool", "Status",
                              [3, 4, 5, 6, 7, 8, 9, 11, 12])
    print("  \n")
    red_pool_tables()


def personal_details_report():
    """
    Calls the function to fetch the data. Displays the
    personal details summary table.
    """
    print("The below table displays the personal")
    print("details of employees added to the redeployment pool.")
    print("It has been sorted according to gender.\n")

    display_redeployment_pool("redeployment_pool", "Gender",
                              [5, 6, 7, 8, 9, 10, 11, 12, 13])
    print("  \n")
    red_pool_tables()


def placed_employees_report():
    """
    Calls the function to fetch the data. Displays the
    placed employees summary table.
    """
    print("The below table displays the employees")
    print("who have been placed in new positions.\n")

    display_redeployment_pool("placed_employees", "New Department",
                              [5, 6, 7, 8])
    print("  \n")
    red_pool_tables()


def department_position_report():
    """
    Calls the function to fetch the data. Displays the
    department and position summary table.
    """
    print("The below table displays the employees")
    print("departments and positions.")
    print("This is before placement.\n")

    display_redeployment_pool("redeployment_pool", "Department",
                              [3, 4, 7, 8, 9, 10, 11, 12, 13])
    print("  \n")
    red_pool_tables()


def salary_comparison_report():
    """
    Calls the function to fetch the data. Displays the
    salary comparison summary table.
    """
    print("The below table displays the")
    print("placed employees salary comparisons.")
    print("It is sorted by Salary Status.\n")

    display_redeployment_pool("placed_employees", "Salary Status",
                              [3, 4])
    print("  \n")
    red_pool_tables()


def days_within_pool_report():
    """
    Calls the function to fetch the data. Displays the
    days within the pool summary table.
    """
    print("The below table displays the")
    print("number of days each employee")
    print("was in the redeployment pool.\n")

    display_remove_rows("redeployment_pool", "Days within Pool",
                        [3, 4, 5, 6, 7, 8, 9])
    print("  \n")
    red_pool_tables()


def salary_and_tenure_report():
    """
    Calls the function to fetch the data. Displays the
    salary and tenure summary table.
    """
    print("The below table displays the")
    print("salary and tenure of the employees.")
    print("These figures are used in the")
    print("retrenchment package calculation.\n")

    display_redeployment_pool("redeployment_pool", "Monthly Salary",
                              [3, 4, 5, 6, 10, 11, 12, 13])
    print("  \n")
    red_pool_tables()


def retrenched_report():
    """
    Calls the function to fetch the data. Displays the
    retrenched employees summary table.
    """
    print("The below table displays the")
    print("retrenched employees.")
    print("These retrenchment package")
    print("calculation is (Salary * Tenure(years)) + (Salary * Months/12).\n")

    display_redeployment_pool("retrenched_employees", "Retrenchment Package",
                              [])
    print("  \n")
    red_pool_tables()


def red_pool_tables():
    """
    Utilises inquirer to provide the user a list of
    the available reports. Calls the relevant function
    based on the report selected to display within terminal.
    """
    while True:
        tables_select = [inquirer.List("tables",
                                       message="Please select the table you"
                                               " wish to view",
                                       choices=["Redeployment Pool Summary",
                                                "Personal Details Summary",
                                                "Department and Position",
                                                "Placed Employees",
                                                "Salary Comparison",
                                                "Days within Pool",
                                                "Salary and Tenure",
                                                "Retrenched Employees",
                                                "Return to Main Menu"],), ]
        answers = inquirer.prompt(tables_select)
        break
    selection = answers["tables"]
    if selection == "Redeployment Pool Summary":
        summary_report()
    elif selection == "Personal Details Summary":
        personal_details_report()
    elif selection == "Department and Position":
        department_position_report()
    elif selection == "Placed Employees":
        placed_employees_report()
    elif selection == "Salary Comparison":
        salary_comparison_report()
    elif selection == "Days within Pool":
        days_within_pool_report()
    elif selection == "Salary and Tenure":
        salary_and_tenure_report()
    elif selection == "Retrenched Employees":
        retrenched_report()
    elif selection == "Return to Main Menu":
        main()


# The below function calls the main menu from which the user
# selects the relevant actions to follow


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
                                            "Data Tables",
                                            "Exit the process"]), ]
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
    elif selection == "Data Tables":
        return red_pool_tables()
    elif selection == "Exit the process":
        print("Thank you for your time.")


print("  \n")
print("Welcome to the capture screen for the Redeployment Process.\n")
get_gender()
