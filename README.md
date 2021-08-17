# Redeployment Process

The redeployment process is utilised by a company undergoing change which results in certain positions becoming redundant. The application will be utilised to add affected employees to a redeployment pool, update employee details, place employees in new positions or retrench employees.

![redeployment-process-mockup](https://github.com/Claire-Potter/Redeployment-Process/blob/98c1262e8a1b196a85e1560c0cc525df2268e63a/read-me-content/mock-up-image.PNG)

<a href="https://redeployment-process.herokuapp.com/" target="_blank">Click Here</a> to access the site.

## Table of Contents

<!-- Start Document Outline -->

* [UX Design](#ux-design)

	* [Redeployment Process](#redeployment-process)
	* [User Stories](#user-stories)
	* [Strategy](#strategy)
		* [High-level Business Goals](#high-level-business-goals)
		* [Value](#value)
		* [Trade-offs](#trade-offs)
	* [Scope](#scope)
	  * [Feature Trade Off](#feature-trade-off)
	  * [Release One Functional Requirements](#release-one-functional-requirements)
	    * [Delivery Constraints](#delivery-constraints)
	* [Structure](#structure)
		* [Information Architecture](#information-architecture)
	* [Skeleton](surface)
	  * [Design Differences](#design-differences)
	* [Surface](#surface)
* [Technologies](#technologies)
* [Features](#features)
* [Testing](#testing)
	* [Features Testing](#features-testing)
	* [Bugs and Issues](#bugs-and-issues)
	* [User Stories Testing](#user-stories-testing)
	* [Code Validation](#code-validation)
	* [Deployment Testing](#deployment-testing)
* [Deployment](#deployment)
	* [Development Interface](#development-interface)
	* [Maintaining Code](#maintaining-code)
	* [Page Deployment](#page-deployment)
	* [How to Fork the Repository](#how-to-fork-the-repository) 
* [References](#references)
	* [Code](#code)
	* [Content](#content)
* [Acknowledgments](#acknowledgments)

<!-- End Document Outline -->

# The Redeployment Process

Please follow the below link to view the redeployment process:

 <a href="https://github.com/Claire-Potter/redeployment-process/blob/main/read-me-content/redeployment-pool-process.pdf">The Redeployment Process</a>

# UX Design

### User Stories

1. The user is a person who works within the HR job family who is required to maintain the redeployment pool.
2. The user will need to select between various actions in order to proceed.
3. The first action should be to add a new employee to the redeployment pool.
4. The user should be required to input or select the various data required to add an employee.
5. All data captured should pass the specific validations in place to ensure accuracy.
6. Once all fields are captured, the data should be consolidated into one list and saved to the redeployment pool database found in google sheets.
7. The second action available should be to update the data of an employee within the redeployment pool.
8. The user should be able to select the employee through the employee number as the unique identifier.
9. If the employee is no longer active within the redeployment pool, the user should not be able to select them.
10. The user should be able to select which field they wish to update.
11. Once the field is selected, the necessary function to update the data should run.
12. The user should be given the option to update another field or to return to the main menu.
13. The next action the user should be able to perform is to place an employee.
14. The place action should allow the user to place an employee within a new position in a new department.
15. The user should be able to select whether the employee received a change in salary or not.
16. The difference between old salary and new salary should be calculated.
17. All data captured should be consolidated and added to the placed employees sheet within the workbook.
18. The relevant fields within the redeployment pool should be updated with the new data.
19. The user should be able to action a retrenchment.
20. The user should be able to select an employee from within the redeployment pool to retrench.
21. This employee cannot have the status placed or retrenched already.
22. Once the employee is selected, the retrenchment package should be calculated utilising information from within the redeployment pool.
23. The data should be consolidated and saved to the retrenched employees sheet within the workbook.
24. The user should be able to view the data available in google sheets via the command-line application.


## Strategy

I have taken some time to answer the following high-level strategic questions:

 1. Is the content culturally appropriate? 

	The content needs to be instructional and professional. It is aimed at an English speaking business audience.

 2. Is the content relevant? 
 

 - The content is made up of the following:
   - An initial home menu, which provides clear instruction and the ability to select an action to proceed with.
   - The four actions - add, update, place and retrench. Each action requires an appropriate description and instruction. All validations require clearly written error messages. When the functions are running, appropriate updates should be provided to keep the user in the loop.
   - The data tables - the data tables should clearly display the relevant data as captured by the user. They should be appropriately labeled according to what data is displayed.

 3. Can we track and catalogue the content in an intuitive way? 

  - The content is coded in python and thus displays within the command-line application. This is because it is a back-end language utilised to collect data and accurately update the database.
 - As a user begins the process, they will first encounter the main menu which provides them with the option to perform the four actions, view the data tables or exit the process. 
 - The first action will allow them to add a user to the redeployment pool. It logically goes through the fields, asking for the correct data and validating before consolidating and adding it back to the redeployment pool. Once complete the user will be taken back to the main menu. 
 - The second action will allow the user to update an employee within the redeployment pool. It only displays employees who are active within the pool, as once they are placed or retrenched, their data should no longer be changed. The user has the choice to continue to update different fields or to return to the menu.
 - The third action allows the user to place the employee into a new position. This asks for new department, position and salary information and calculates the difference in salary. The user is asked each question in a logical order. Once again, only employees who are active within the pool can be selected. The user will be returned to the main menu when done.
 - The fourth action enables the user to retrench an employee. This will be performed by selecting an active employee, the function will then calculate the retrenchment package and add the information to the database. The user will be directed back to the main menu when done.
 - The next option on the main menu is to view data tables. This will take the user to a menu of tables to select from. These are labeled according to the data that they display and will print the table to the command line. The setup is clear and simple to enable the user to view the necessary data clearly.
 - The final option is to exit the process which will exit the user from the redeployment process.

 4. Is the technology appropriate?  
	 
	 The process is coded in Python. The database is setup in google sheets. The following libraries are used to provide the necessary functionality:
	 - gspread
	 - inquirer - changed to InquirerPy
	 - prompt_toolkit - InquirerPy is dependent on this
	 - pandas
	 - datetime
	 - Python.display
	  
	  Google cloud platform is utilised to create
	  the API between the application and google sheets.
	  
     The user will be able to access the application through the command-line.

### High-level Business Goals

 - Create a functional application to accurately complete the various actions within the redeployment process.
 - Maintain the redeployment database within google sheets.
 - Add validated data to google sheets and return relevant data when requested.
 - Perform all calculations and return correct values.

### Value

The value of the redeployment process application is that it allows the user to fully maintain the redeployment database.
This ensures that the employee data is accurate and can be fed to recruitment systems, payroll and the database can be utilised to create reports and dashboards.
As the database is updated as and when actions occur this provides the company with the ability to provide regular live updates on the redeployment process. It also allows the company to accurately track placement costs/savings, retrenchment costs and the ultimate value provided by the redeployment process. Additional to this, all data is validated ensuring accuracy and avoiding duplication.

### Trade-offs

Using the trade-off process to rank the importance and feasibility of the opportunities I have decided:

1. To go ahead with 10/13 of the opportunities.
2. I will not be creating a front end site to complete the process on as this is a minimum viable product.
3. This would be a future opportunity to explore.

![Table depicting the Importance rating vs. the Feasibility rating per Opportunity](https://github.com/Claire-Potter/redeployment-process/blob/main/read-me-content/trade-offs-table.PNG)
   

## Scope
To provide a redeployment application to be utilised to add affected employees to a redeployment pool, update employee details, place employees in new positions or retrench employees. To be able to update the google sheets database as well as return data when required.

### Feature Trade Off

 <a href="https://github.com/Claire-Potter/redeployment-process/blob/main/read-me-content/feature-trade-offs.PNG">Feature Trade Off Table</a>


This site will be developed as a minimum viable product. Future releases could include additional functionality depending on the success of the first release. This could include a front-end website to complete the process on as well as generate the tables and data charts.

### Release One Functional Requirements

1. Command-line application
2. Main menu prompting the user to choose an action
3. Function/s to add a new employee to the redeployment pool.
4. Function/s to update an employee record within the redeployment pool.
5. Function/s to place an employee as recruited to a new position.
6. Function/s to retrench an employee.
7. Provide a list of employee numbers for the user to select an employee.
8. Validate the list so that only active employees are displayed.
9. All data fields should be validated when captured.
10. Value Errors should display if incorrect data is captured.
11. Save all data captured to the correct sheet within google sheets.
12. Return the correct data when required to the command-line.
13. Summarised versions of the data tables should be displayed in the command line when called.
14. The difference in salaries for placed employees should be calculated.
15. The days within the pool figure should be calculated.
16. The retrenchment package should be calculated.

#### Delivery Constraints

1. Skill - This is the developer's first time working in Python so this presents a learning curve.
2. Time - limited time to complete and deliver the site.

## Structure
Development conventions and best practice have been applied as far as possible to ensure that user expectations are met. The breakdown of the structure is available further down in this document within the features section.

### Information Architecture

![Application Hierarchy ](https://github.com/Claire-Potter/redeployment-process/blob/main/read-me-content/skeleton.jpeg)


## Skeleton 

Please follow the below link to view the wireframes for the application:

 <a href="https://github.com/Claire-Potter/redeployment-process/tree/main/read-me-content/wireframes">Wireframes</a>

### Design differences

1. Due to issues with the library inquirer, the library InquirerPy was utilised as this uses the latest python version and readchar version. Functions were updated to use the InquirerPy library.
2. An additional validation was included within the start date validation function to ensure that the date is less than today's date. This is to prevent errors when calculating number of days in pool, as the exit date is set as today's date.
3. The employee number as the selector was changed to be the employee number, the employee name and the employee surname. This is to improve the user experience, as a user would be more familiar with an employee's name than their number. It also 'humanises' the process. It is a very sensitive process and it is important to always have the employee's interests at heart. By including their names, it ensures that the user capturing the data relates each action to a person, rather than working transactionally.
4. All of the data tables were updated to display the name and surname of the employee. This was completed for the same reason as number 3.

## Surface

As this application is written in Python and displays within the command line, visual design aspects catered for through html and css were minimal and provided for within the Code Institute Python template.

## Technologies

The process is coded in Python. The database is setup in google sheets. The following libraries are used to provide the necessary functionality:
- gspread
- inquirer - changed to InquirerPy
- prompt_toolkit - InquirerPy is dependent on this
- pandas
- datetime
- IPython.display
	  
Google cloud platform is utilised to create the API between the application and google sheets.

The user will be able to access the application through the command-line.

Other technologies:

1. Lucidchart - https://lucid.app/lucidchart
 	* To create the process
2. Gitpod
	* Platform used to develop and test site.
3. Github
	* Platform used to host repository and deployed site.
4. Markdown Monster
	* Used to edit Markdown



# Features

The Redeployment Process app consists of the following Features:

* [Features](#features)
	* [Command Line Interface](#command-line-interface)
	* [Main Menu](#main-menu)
	* [Add Employee](#add-employee)
	* [Update Employee](#update-employee)
	* [Place Employee](#place-employee)
	* [Retrench Employee](#retrench-employee)
	* [Data Tables](#data-tables)
	* [Features Left to Implement](#features-left-to-implement)
	    
## Command Line Interface

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/01.command-line-interface.PNG" 
     alt="command line interface" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 


The application is accessible through a command line interface, allowing the user to capture input and make selections according to the python code.

## Main Menu

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/02.main-menu.PNG" 
     alt="main menu" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 


The InquirerPy  library is utilised to provide a main menu from which the user can select the necessary action that they wish to perform.
This menu is the central starting and ending point of the application and provides access to the various actions available to the user. 
Once an action is complete the main menu will be called to display again so that the user has the opportunity to perform another available action. This is to prevent the user from having to continuously re-run the application after each action. It streamlines the process.

To end the application the user simply selects Exit the process. They will be thanked for their time and the application will end.

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/03.exit-process.PNG" 
     alt="exit process" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
   
## Add Employee

The Add Employee Action is selected to add a new employee to the redeployment pool. The function will call the various functions to capture the necessary data and validate it. It will then call the function to save the new employee details as a row to the google sheets worksheet.


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/04.employee-number.PNG" 
     alt="Add Employee - Employee Number" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
 
 The employee number is captured by the user as a six digit unique number. The validations in place will ensure that the number is six digits long and only consists of numeric characters. It will also compare the number to the existing employee numbers within the google sheets database to ensure it is a unique value. The employee number is left as a string and added to google sheets this way as it is better to use a string to look up other data than an integer.
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/05.first-name.PNG" 
     alt="Add Employee - Name" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The first name field is utilised to capture the first name of the employee. The data cannot be numeric. It does allow special characters as often names contain a dash -, a space, or pronunciation emphasis characters. When the first name is captured, the first letter of the name will be capitalised by the application and it will be saved as a string.

 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/06.surname.PNG" 
     alt="Add Employee - Surname" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The surname field is utilised to capture the surname of the employee. The same function to validate the first name is used to validate the surname, the first letter of the surname will be capitalised by the application and it will be saved as a string.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/07.age.PNG" 
     alt="Add Employee - Age" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The age field is utilised to capture the age of the employee. The user is provided with an age range of 18 - 75 and they need to enter an age within this range. The validation function will ensure that the data is numeric and falls within the given range, otherwise a value error will occur. The age field is converted to an integer and saved.

 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/08.gender.PNG" 
     alt="Add Employee - Gender" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
InquirerPy is utilised once again to capture the gender of the employee. The user is provided with a list of values and they need to select one of the provided options. Validations are not required as the data is already provided for the user to choose from. The gender field is saved as a string.



 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/09.department.PNG" 
     alt="Add Employee - Department" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The Department field is utilised to capture the business department of the employee. The same function used to validate text fields is utilised again here, the first letter of the department will be capitalised by the application and it will be saved as a string.



 
  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/10.position.PNG" 
     alt="Add Employee - Position" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The Position field is utilised to capture the current position filled by the employee. The same function used to validate text fields is utilised again here, the first letter of the position will be capitalised by the application and it will be saved as a string.


 
  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/11.salary.PNG" 
     alt="Add Employee - Salary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The salary field is utilised to capture the current salary of the employee. The user is provided with a salary range of 100 - 100 000 and they need to enter a salary within this range. The validation function will ensure that the data is numeric and falls within the given range, otherwise a value error will occur. The salary is converted to an integer and saved.


 
  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/12.tenure-years.PNG" 
     alt="Add Employee - Tenure - years" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The years of service field is utilised to capture the number of years of service of the employee. The user is provided with a  range of 1 - 50 and they need to enter a number within this range. The validation function will ensure that the data is numeric and falls within the given range, otherwise a value error will occur. The years of service field is converted to an integer and saved. This value is later utilised to calculate the redeployment package. It remains as a fixed value and will not include the additional time spent in the redeployment pool.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/13.tenure-months.PNG" 
     alt="Add Employee - Tenure - months" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The months of service field is utilised to capture the number of months of service of the employee. The user is provided with a  range of 1 - 11 and they need to enter a number within this range. The validation function will ensure that the data is numeric and falls within the given range, otherwise a value error will occur. The months of service field is converted to an integer and saved. This value is later utilised to calculate the redeployment package. It remains as a fixed value and will not include the additional time spent in the redeployment pool.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/14.start-date.PNG" 
     alt="Add Employee - Start Date" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
The start date / entry date field is utilised to capture the start date that the employee is added to the redeployment pool / begins the redeployment process. The date is validated to ensure it is captured in the format dd/mm/yyyy. An additional validation is in place to ensure that the date is less than today's date. This is to ensure that the calculation of number of days in the pool which happens when an employee is placed or retrenched will not error, as the exit date from the pool is captured as the current date, so the start date needs to be smaller than this date. A value error will occur if the date is captured incorrectly.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/15.update-messages.PNG" 
     alt="Add Employee - Update Message" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

Once all of the fields are captured, the user will be notified that the application is busy updating the redeployment pool worksheet with the record. The user will be informed when this has been successfully saved and they will be returned to the main menu.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/16.data-added-to-worksheet.PNG" 
     alt="Add Employee - added to sheet" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
All of the data will be added in the correct order to a list and the application will call the function to add the new employee record as a row to the worksheet redeployment_pool  within the google sheet, thereby successfully updating the database.

## Update Employee

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/17.update-employee.PNG" 
     alt="update employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

The user can select the option update employee details, this will call a list containing the active employees within the redeployment pool. Once an employee has been placed or retrenched, their data can no longer be updated, as the redeployment process has been completed for them.


The user will be presented with the list of active employees which contains the employee number, the first name and the surname. They can select the relevant employee to update. The employee number will be saved as a reference to select the correct record within google sheets to update.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/18.update-options.PNG" 
     alt="update options" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
	    
Once an employee has been selected, the user will be presented with a list of options to choose from. These are the various data fields within the redeployment pool. Each option will call the relevant function, as per the functions used within the add employee action, to update and validate the new value for the field.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/19.update-capture.PNG" 
     alt="update captured" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
	    
The user will utilise the input field to capture the new value.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/20.update-complete-return-to-menu.PNG" 
     alt="update complete return to menu" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
Once the user has entered their update, the application will save the data change to the sheet and let the user know once completed. The user will be presented with the option to select whether they would like to return to the update options menu to update another record. If they select yes, the update action will run again. If they select no, they will be returned to the main menu.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/21.update-saved.PNG" 
     alt="updated cell" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
             ">
             
Only the cell that has been updated by the user will be changed within the google sheet. All other values will remain the same.

## Place Employee

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/22.place-employee-select.PNG" 
     alt="place employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

When the user selects the action to place an employee, the select employee menu with the active employees is returned. The user can then select the relevant employee to place.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/23.change-in-salary.PNG" 
     alt="change in salary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
	    
The user is asked if there has been a change in the employee's salary. They can select if it has been decreased, remained the same or increased. The users selection is saved.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/24.new-department.PNG" 
     alt="new department" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
The user is requested to capture the new department of the employee. This will be the department that the employee has been placed within.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/25.new-position.PNG" 
     alt="new position" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
The user is requested to capture the new position of the employee. This will be the position that the employee has been recruited into.


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/26.new-salary-and-difference.PNG" 
     alt="new salary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
The user is requested to capture the new salary of the employee. If the salary has decreased they will need to capture a salary that is less than the current salary. If the salary has been increased, they will need to capture a salary that is greater than the current salary. If the salary has remained the same, they will not have to recapture it. The difference will be calculated as 0.


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/27.placed-messages.PNG" 
     alt="placed messages" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
The user will be thanked for capturing the placement. They will be provided with updates as the application goes through the process of  saving the new record to the placed employees sheet, calculating the number of days within the pool, and updating the data within the redeployment pool.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/28.placed-employee.PNG" 
     alt="placed employee sheet" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
The employee record will be added to the placed employee worksheet within google sheets.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/29.redeployment-pool-updated.PNG" 
     alt="redeployment pool employee placed update" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
The employee record within the redeployment pool worksheet will have the exit date added as the current date, the days within the pool will be calculated and added and the status will be updated as Placed.

The user will be returned to the main menu.

## Retrench Employee

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/30.retrench-employee.PNG" 
     alt="retrench employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
When a user selects to retrench an employee, the employee menu will display for the user to select an employee from. Note that the employee Dale Jason, who was placed, no longer reflects on the menu as his status is no longer active.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/31.retrench-employee-update-messages.PNG" 
     alt="retrench employee - updates" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

 The user will be informed that the application is calculating the retrenchment package.This is done by fetching the salary, the Tenure - years and months values from the redeployment pool worksheet. The following calculation is then performed. Tenure-years * Monthly Salary + (Tenure-months / 12 * Monthly Salary). They will be provided with updates as the application goes through the process of  saving the new record to the retrenched employees sheet, calculating the number of days within the pool, and updating the data within the redeployment pool.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/32.retrench-employee-update-redeployment-pool.PNG" 
     alt="retrenched employee sheet" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
The employee record will be added to the retrenched employee worksheet within google sheets.

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/33.retrenched-employee.PNG" 
     alt="redeployment pool employee retrenched update" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
The employee record within the redeployment pool worksheet will have the exit date added as the current date, the days within the pool will be calculated and added and the status will be updated as Retrenched.

The user will be returned to the main menu.

 ## Data Tables
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/34.data-tables-menu.PNG" 
     alt="data tables menu" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
When the user selects the option Data Tables they are taken to the above data table menu containing the various tables that can be displayed. It is very useful for the  user to be able to call the various tables to view the data, as it allows them to check updates to the redeployment pool, check calculations and have the data at hand, as per live capture, if questioned.

Each option displays the relevant table as follows:

Redeployment Pool Summary


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/35.redeployment-pool-summary.PNG" 
     alt="redeployment pool summary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
 Personal Details Summary
 
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/36.personal-details-summary.PNG" 
     alt="personal details summary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
Department and Position


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/37.department-and-position.PNG" 
     alt="department and position" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
 Placed employees
 
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/38.placed-employees.PNG" 
     alt="placed employees" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
Salary Comparison


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/39.salary-comparison.PNG" 
     alt="salary comparison" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
Days within Pool


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/40.days-within-pool.PNG" 
     alt="days within pool" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
Salary and Tenure


<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/41.salaries-and-tenure.PNG" 
     alt="salary and tenure" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
Retrenched Employees


<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/42.retrenched-employees.PNG" 
     alt="retrenched employees" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
## Features Left to Implement

The following features could potentially be implemented in future releases:
1. Create a front-end application to display the data tables, as well as utilise the database to create charts displaying the various values, calculated differences, statistics etc. This would be an excellent reporting tool to track and report on the redeployment process.
2. Create a front-end application to complete the redeployment process via. Instead of capture taking place within the command line, a front-end application, with user login and validation could be created to complete the process via.

# Testing

### Features Testing

## Main Menu

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/00.main-menu.PNG" 
     alt="main menu" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 


1. Main Menu loads correctly when app runs: PASS
2. Main Menu options do not contain spelling errors and are clear to understand: PASS
3. Main Menu options all call the correct function as per label: PASS
4. Main Menu options run the functions without errors: PASS
5. Main Menu option "Exit the process" correctly end the application: PASS



   
## Add Employee

1. When Add Employee is selected from the main menu the first request to user is to capture the employee number. It displays correctly, with no errors or spelling mistakes: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/04.employee-number.PNG" 
     alt="Add Employee - Employee Number" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
 2. The user is able to capture their input: PASS
 3. The validation to ensure that the employee number is numeric runs correctly and displays as error message: PASS

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/01.non-numeric-entry.PNG" 
     alt="non-numeric" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
 4. The validation to ensure that the employee number contains exactly six digits runs correctly and displays as error message: PASS

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/02.longer-than-6-digits.png" 
     alt="six-digits" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/03.shorter-than-6-digits.PNG" 
     alt="shorter -six-digits" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
5. The  validation to ensure that the employee number is unique runs correctly and displays as error message: PASS

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/04.unique-employee-number.PNG" 
     alt="employee number unique" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 


 6. The employee number is added a s a string to the sheet: PASS
 
 <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/05.employee-number-as-string.PNG" 
     alt="employee number string" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
 
 7. The request for the first name is asked next. It displays correctly, with no errors or spelling mistakes:PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/05.first-name.PNG" 
     alt="Add Employee - Name" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
8. The data cannot be numeric. An appropriate error message will display: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/06.first-name-no-numbers.PNG" 
     alt="Add Employee - Name numeric" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

9. It does allow special characters as often names contain a dash -, a space, or pronunciation emphasis characters: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/07.name-allows-characters.PNG" 
     alt="Add Employee - name characters" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

10. When the first name is captured, the first letter of the name will be capitalised by the application and it will be saved as a string: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/08.first-name-capitalised.PNG" 
     alt="Capitalised and string" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

            
 11. The request for the surname name is asked next. It displays correctly, with no errors or spelling mistakes:PASS
 
      <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/06.surname.PNG" 
     alt="Add Employee - Surname" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">  

            
12. The data cannot be numeric. An appropriate error message will display: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/09.surname-no-numbers.PNG" 
     alt="Add Employee - Surname numeric" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

13. It does allow special characters as often names contain a dash -, a space, or pronunciation emphasis characters: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/10.surname-allows-characters.PNG" 
     alt="Add Employee - Surname characters" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

14. When the surname is captured, the first letter of the name will be capitalised by the application and it will be saved as a string: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/11.surname-capitalised.PNG" 
     alt="Capitalised and string" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
15. The add employee function will now request the user to capture the age of the employee. This displays correctly with no errors or spelling mistakes and user can capture their input: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/07.age.PNG" 
     alt="Add Employee - Age" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
16. The user is provided with an age range of 18 - 75 and they need to enter an age within this range. If they capture a value less than the minimum age it will fail and provide an error message: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/12.age-younger.PNG" 
     alt="Add Employee - Age younger" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
17. If they capture a value greater than the maximum age it will fail and provide an error message: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/13.age-older.PNG" 
     alt="Add Employee - Age older" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
18. If they capture a non-numeric value it will fail and provide an error message: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/14.age-non-numeric.PNG" 
     alt="Add Employee - Age non-numeric" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
19. The age field is converted to an integer and saved correctly to the sheet: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/15.age-integer-saved.PNG" 
     alt="Add Employee - Age saved" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
20. The user is provided with the option to select the gender of the employee. It displays correctly, without errors or spelling mistakes: PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/08.gender.PNG" 
     alt="Add Employee - Gender" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
21. Validations are not required as the data is already provided for the user to choose from. The user can select an option and proceed: PASS

22.  The gender field is saved as a string to the sheet: PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/16.gender-string.PNG" 
     alt="Add Employee - Gender - string" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

23. The Department field is utilised to capture the business department of the employee. It displays correctly, without errors or spelling mistakes: PASS

 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/09.department.PNG" 
     alt="Add Employee - Department" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
           
24. The same function used to validate the text fields - first name and surname is utilised again here, a numeric value cannot be captured: PASS

25. the first letter of the department will be capitalised by the application and it will be saved as a string: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/17.department-as-string.PNG" 
     alt="Add Employee - Department as string" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

26. The Position field is utilised to capture the current position filled by the employee. It displays correctly, with no errors or spelling mistakes: PASS

  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/10.position.PNG" 
     alt="Add Employee - Position" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
27. The same function used to validate text fields is utilised again here, a numeric value won't be accepted: PASS

28. the first letter of the position will be capitalised by the application and it will be saved as a string: PASS

  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/18.position-string.PNG" 
     alt="Add Employee - Position-string" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

29. The salary field is utilised to capture the current salary of the employee. It displays correctly, without errors or spelling mistakes: PASS
 
  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/11.salary.PNG" 
     alt="Add Employee - Salary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
 30. The user is provided with a salary range of 100 - 100 000 and they need to enter a salary within this range. If the salary is too low it  will display an error: PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/20.salary-too-low.PNG" 
     alt="Add Employee - Salary low" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
 31. If the salary is too high it  will display an error: PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/19.salary-too-high.PNG"
     alt="Add Employee - Salary high" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
 
32. The validation function will ensure that the data is numeric, the below example, a space has been added, if non-numeric it will fail: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/21.salary-with-space.PNG" 
     alt="Add Employee - Salary non-numeric" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
 
33. The salary field is converted to an integer and saved: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/22.salary-as-integer.PNG" 
     alt="Add Employee - Salary integer saved" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

34. The years of service field is utilised to capture the number of years of service of the employee. It displays correctly without errors or spelling errors: PASS
 
  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/12.tenure-years.PNG" 
     alt="Add Employee - Tenure - years" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
35. The user is provided with a  range of 1 - 50 and they need to enter a number within this range. If the number is too low it will fail: PASS

  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/23.years-too-low.PNG" 
     alt="Add Employee - Tenure - years too low" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

36.  The validation function will ensure that the data is numeric and falls within the given range, otherwise a value error will occur such as if it is too high: PASS

  <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/24.years-too-high.PNG" 
     alt="Add Employee - Tenure - years too high" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

37.  The years of service field is converted to an integer and saved: PASS

38.  The months of service field is utilised to capture the number of months of service of the employee. It displays correctly, without errors or spelling mistakes: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/13.tenure-months.PNG" 
     alt="Add Employee - Tenure - months" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
39.The user is provided with a  range of 1 - 11 and they need to enter a number within this range. If the number is too low it will fail: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/25.months-too-low.PNG" 
     alt="Add Employee - Tenure - months low" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 


40. The validation function will ensure that the data is numeric and falls within the given range, otherwise a value error will occursuch as if it is too high: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/26.months-too-high.PNG" 
     alt="Add Employee - Tenure - months high" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
41.  The months of service field is converted to an integer and saved: PASS

42. The start date / entry date field is utilised to capture the start date that the employee is added to the redeployment pool / begins the redeployment process. It displays correctly with no errors or spelling mistakes: PASS 

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/14.start-date.PNG" 
     alt="Add Employee - Start Date" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
            
 43. The date is validated to ensure it is captured in the format dd/mm/yyyy: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/27.incorrect-date-format.PNG" 
     alt="Add Employee - Start Date incorrect" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
 
 44. An additional validation is in place to ensure that the date is less than today's date: PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/28.incorrect-too-great-date.PNG" 
     alt="Add Employee - Start Date greater than today" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
45. The date is saved correctly to the sheet: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/29.saved-correctly-to-sheets.PNG" 
     alt="Add Employee - Start Dat saved correctly" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

46. The employee record is saved as a row to the end of the correct worksheet - redeployment_pool. All of the data matches up to the correct column: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/30.employee-record-saved.PNG" 
     alt="Add Employee - added to sheet" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
47. The user will be returned to the main menu: PASS

## Update Employee

1. When the user selects the action to update an employee, the select employee menu with the active employees is returned. It displays correctly, without errors or spelling mistakes. It contains the employee number, the employee name and the empoyee surname: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/17.update-employee.PNG" 
     alt="update employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;"> 

2. It does not display the placed or retrenched employees: PASS

3. The user can then select the relevant employee to update: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/31.select-an-employee.PNG" 
     alt="select employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;"> 

4. Once an employee has been selected, the user will be presented with a list of options to choose from. It displays correctly, without errors or spelling mistakes: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/18.update-options.PNG" 
     alt="update options" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
	    
5. The options are the various data fields within the redeployment pool. Each option calls the relevant function, as per the functions used within the add employee action, to update and validate the new value for the field: PASS
6. Once the user has entered their update, the application will save the data change to the sheet and let the user know once completed: PASS
7. The user will be presented with the option to select whether they would like to return to the update options menu to update another record: PASS
8. If they select yes, the update action will run again: PASS
9. If they select no, they will be returned to the main menu: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/19.update-capture.PNG" 
     alt="update captured" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 

             
10. Only the cell that has been updated by the user will be changed within the google sheet. All other values will remain the same: PASS

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/21.update-saved.PNG" 
     alt="updated cell" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
             ">

## Place Employee

1. When the user selects the action to place an employee, the select employee menu with the active employees is returned. It displays correctly, without errors or spelling mistakes. It contains the employee number, the employee name and the empoyee surname: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/22.place-employee-select.PNG" 
     alt="place employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
2. It does not display the placed or retrenched employees: PASS

3. The user can then select the relevant employee to place: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/31.select-an-employee.PNG" 
     alt="select employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;"> 
	    
4. The user is asked if there has been a change in the employee's salary. They can select if it has been decreased, remained the same or increased. The menu displays correctly, without errors or spelling mistakes: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/23.change-in-salary.PNG" 
     alt="change in salary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            "> 
	    
	    
5. The users selection is saved to be referenced again: PASS
6. The user is requested to capture the new department of the employee. This will be the department that the employee has been placed within and calls the same function to add a department for a new employee: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/24.new-department.PNG" 
     alt="new department" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
7. The user is requested to capture the new position of the employee. This will be the position that the employee has been recruited into and calls the same function to add a position for a new employee: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/25.new-position.PNG" 
     alt="new position" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
8. The user is requested to capture the new salary of the employee. If the salary has decreased they will need to capture a salary that is less than the current salary: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/32.placed-salary-decrease.PNG" 
     alt="salary decrease" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
9. If the salary has been increased, they will need to capture a salary that is greater than the current salary: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/33.placed-salary-increase.PNG" 
     alt="salary increase" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
10. If the salary has remained the same, they will not have to recapture it. The difference will be calculated as 0: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/34.placed-salary-the-same.PNG" 
     alt="salary the same" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
11. The difference between the salaries is calculated correctly: PASS
	    
12. The user will be thanked for capturing the placement. They will be provided with updates as the application goes through the process of  saving the new record to the placed employees sheet: PASS
13. The days within the pool are calculated correctly: PASS
14. The status is captured as Placed and the record is updated within the redeployment pool sheet: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/27.placed-messages.PNG" 
     alt="placed messages" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
15. The employee record will be added as a row to the placed employee worksheet within google sheets. The data will align with the columns in the sheet: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/28.placed-employee.PNG" 
     alt="placed employee sheet" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
16. The employee record within the redeployment pool worksheet will have the exit date added as the current date, the days within the pool will be calculated and added and the status will be updated as Placed: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/29.redeployment-pool-updated.PNG" 
     alt="redeployment pool employee placed update" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	       
17. The user will be returned to the main menu: PASS

## Retrench Employee

1. When a user selects to retrench an employee, the employee menu will display for the user to select an employee from. This will display correctly, without errors or spelling mistakes: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/30.retrench-employee.PNG" 
     alt="retrench employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
2. It does not display the placed or retrenched employees: PASS

3. The user can then select the relevant employee to place: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/31.select-an-employee.PNG" 
     alt="select employee" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;"> 	    


 4. The user will be informed that the application is calculating the retrenchment package.This is done by fetching the salary, the Tenure - years and months values from the redeployment pool worksheet. The following calculation is then performed. Tenure-years * Monthly Salary + (Tenure-months / 12 * Monthly Salary). This is calculated correctly: PASS

 5.  They will be provided with updates as the application goes through the process of  saving the new record to the retrenched employees sheet, calculating the number of days within the pool, and updating the data within the redeployment pool: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/31.retrench-employee-update-messages.PNG" 
     alt="retrench employee - updates" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

6. The employee record will be added to the retrenched employee worksheet within google sheets as a new row. All data will align with the columns: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/32.retrench-employee-update-redeployment-pool.PNG" 
     alt="retrenched employee sheet" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
7. The employee record within the redeployment pool worksheet will have the exit date added as the current date, the days within the pool will be calculated and added and the status will be updated as Retrenched: PASS

   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/33.retrenched-employee.PNG" 
     alt="redeployment pool employee retrenched update" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	        
8. The user will be returned to the main menu: PASS

 ## Data Tables
 
1. When the user selects the option Data Tables they are taken to the data table menu containing the various tables that can be displayed. This displays correctly, without errors or spelling mistakes: PASS
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/34.data-tables-menu.PNG" 
     alt="data tables menu" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
2. The Redeployment Pool Summary returns the following fields: Employee Number, Name, Surname, Entry Date, Status. The data is sorted by Status: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/35.redeployment-pool-summary.PNG" 
     alt="redeployment pool summary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
3.  Personal Details Summary returns the following fields: Employee Number, Name, Surname, Age, Gender. The data is sorted by gender: PASS
 
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/36.personal-details-summary.PNG" 
     alt="personal details summary" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
4. Department and Position returns the following fields: Employee Number, Name,  Surname, Department, Position. The data is sorted by department: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/37.department-and-position.PNG" 
     alt="department and position" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
	    
5. Placed employees returns the following fields: Employee Number, Name,  Surname, New Department, New Position.  The data is sorted by department: PASS
 
 
   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/38.placed-employees.PNG" 
     alt="placed employees" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
6. Salary Comparison returns the following fields: Employee Number, Name,  Surname, Old Monthly Salary, New Monthly Salary, Difference, Salary Status. The data is sorted by Salary Status: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/39.salary-comparison.PNG" 
     alt="salary comparison" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
7. Days within Pool returns the following fields:  Employee Number, Name,  Surname, Entry Date, Exit Date, Days within Pool, Status. The data uis sorted by Days within Pool: PASS


   <img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/40.days-within-pool.PNG" 
     alt="days within pool" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
8. Salary and Tenure returns the following fields: Employee Number, Name,  Surname, Monthly Salary, Tenure -years, Tenure -months. The data is sorted by salary: PASS


<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/41.salaries-and-tenure.PNG" 
     alt="salary and tenure" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
            
9. Retrenched Employees returns the following fields: Employee Number, Name,  Surname, Retrenchment Package. The data is sorted by Retrenchment Package: PASS


<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/features/42.retrenched-employees.PNG" 
     alt="retrenched employees" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
10. Return to main menu returns the user to the main menu: PASS

### Bugs and Issues

1. An issue was experienced with the start date field. If I converted the value to a date within the function, it could not be returned to the sheet, a json serializable error would occur:

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/json-serializable-error.PNG" 
     alt="json serializable error" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">
	    
2. If I utilised python code to serialize the date, it would be returned to google sheets in a long and complicated format. I required that the date be added precisely as it is utilised to calculate the days in pool figure.
3. If I added the date to a list with the rest of the values for a new employee, it would be added as a string and contain ' in front.
4. However if I added the string date to the redeployment_pool sheet as an individual cell update, the value would be added without the character ' and sheets would format it accordingly.
5. I could then easily fetch the value and prepare it in python for the days in pool calculation.

### User Stories Testing

1. The user is a person who works within the HR job family who is required to maintain the redeployment pool: 

    PASS - the application utilises common practice phrases, naming conventions and a process that would be familiar to an HR professional.
    
2. The user will need to select between various actions in order to proceed:

   PASS - the main menu provides the user with the various actions to select between.
   
3. The first action should be to add a new employee to the redeployment pool:

    PASS - this is the first action available on the list.
    
4. The user should be required to input or select the various data required to add an employee:

   PASS - the action calls all the relevant functions to update the required data fields.
   
5. All data captured should pass the specific validations in place to ensure accuracy: 

   PASS - all of the data fields have validations in place, unless the value is selected from a set list of values.

6. Once all fields are captured, the data should be consolidated into one list and saved to the redeployment pool database found in google sheets:

    PASS - the data is consolidated and saved as a row to the worksheet.
    
7. The second action available should be to update the data of an employee within the redeployment pool: 
 
   PASS - this is the second action available on the main menu.
  
8. The user should be able to select the employee through the employee number as the unique identifier: 

    PASS - the employee number is provided as the main identifier, the user experience is further enhanced as the first name and surname is also provided.
    
9. If the employee is no longer active within the redeployment pool, the user should not be able to select them:

    PASS - placed or retrenched employees do not appear on the employee selection list.
    
10. The user should be able to select which field they wish to update:

    PASS - the user is presented with all data fields as options within a list which they can select from.
 
11. Once the field is selected, the necessary function to update the data should run:

    PASS - all of the fields call the correct function to update the value.
 
12. The user should be given the option to update another field or to return to the main menu: 

    PASS - once the update has been saved, the user is asked whether they would like to perform another update or to return to the main menu.

13. The next action the user should be able to perform is to place an employee: 

    PASS - placing an employee is the third option available within the main menu.

14. The place action should allow the user to place an employee within a new position in a new department: 

    PASS -the function includes the selection of a new department and a new position for the employee.

15. The user should be able to select whether the employee received a change in salary or not:

     PASS - the user can select if there was a decrease, an increase or if the salary remained the same.
   
16. The difference between old salary and new salary should be calculated: 

    PASS - this is calculated and added as a new field called Difference.

17. All data captured should be consolidated and added to the placed employees sheet within the workbook:

    PASS - the data is added as a new row to the worksheet.
  
18. The relevant fields within the redeployment pool should be updated with the new data:

     PASS - only the affected fields are updated within the redeployment pool sheet.
 
19. The user should be able to action a retrenchment: 

    PASS - this is the fourth option within the main menu.
 
20. The user should be able to select an employee from within the redeployment pool to retrench: 

    PASS - the first function called is to select an employee.
 
21. This employee cannot have the status placed or retrenched already:

     PASS - the employee list only contains active employees.
 
22. Once the employee is selected, the retrenchment package should be calculated utilising information from within the redeployment pool:

     PASS - the salary and tenure information is fetched from the redeployment pool sheet and utilised to calculate the package.
   
23. The data should be consolidated and saved to the retrenched employees sheet within the workbook: 

    PASS - the data is consolidated and added as a new row to the retrenched employees worksheet.

24. The user should be able to view the data available in google sheets via the command-line application:

    PASS - various data tables are available to the user to view the data.

### Code Validation

The run.py file passed through pep-8 online successfully:

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/pep8-online.PNG" 
     alt="pep-8 online pass" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

Pycodestyle ran within the console returned no errors:

<img src="https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/testing/pycodestyle-no-errors.PNG" 
     alt="pycodestyle validation" 
     style="display:block; 
            float:none; 
            margin-left:auto; 
            margin-right:auto;
            ">

### Deployment Testing

An issue was experienced when accessing the deployed site on Heroku. I was able to deploy the site successfully, however,
when I tried to run the site, I received an error that the readchar programme was not working. When I looked into this further
I saw that this was part of the inquirer library. The application was dependent on the inquirer library as it is used multiple
times to create menus and options lists. When researching, I discovered that inquirer only worked on python 3.8 downwards. I tried to creat a runscript to specify that Heroku uses python 3.8.11, as this is what I was using on git. This did not correct the error. I then went through the process of updating from the inquirer library to the InquirerPy library and the latest version of readchar as this is aligned to python 3.9. I also installed node modules via npm to try to cater for the missing functionality. The updates meant that the deployed application no longer generated an error message, however it was still not working. It presented me with a static screen displaying the main menu, but no options could be selected.

I had logged the issue with the tutor team, who were in the process of getting advice from the assessment team and the development team. The development team very kindly created a brand new template for me to utilise to create a new repository from. The changes that they made meant that the InquirerPy function could now be read by the command line interface. I created a new repository using the template and added my run.py and requirements.txt files to the new repository. I then deployed the new version to Heroku. The new application works well! I have included the link to the application from the new repository within this ReadMe, as this is the original repository, it contains the full commit history.

The only additional changes I had to make once deployed, was to summarise the various headings within the worksheets on google sheets and make sure the new names were utilised throughout my code. Due to the width of the screen of the app, the Data Tables needed to be more compact to be able to display well. All other functionality was tested and passed.

The changes made were as follows:

1. Change from Employee Number to Emp Number:

![emp number](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/00.emp-number.PNG)

2. Change the Status Retrenched to Retren.

![Retren.](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/01.redeployment-pool-report.PNG)

3. Shorten the headings New Department and New Position to New Dep and New Pos

![New Dep and Pos](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/03.placed-employees.PNG)

4. Shorten Difference to Diff and change Salary Status to Status

![Salary Status](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/04.salary-comparison.PNG)

5. Shorten Days with Pool to Days

![Days](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/05.days-within-pool.PNG)

6. Shorten Monthly Salary to Salary

![Salary](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/06.salary-and-tenure.PNG)

7. Shorten Retrenchment Package to Package

![Package](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployed-site-changes/07.retrenched-employees.PNG)


# Deployment

## Development Interface

This website was developed on Gitpod using the Code Institute Python student template with changes frequently committed to git then pushed onto GitHub from the Gitpod terminal. The deployed site utilises the new version of the python template.

The deployed version of the website is the master.

## Maintaining Code

To maintain the code the following actions are taken:

1. Log into GitHub
2. Go to the repositories tab at the top of the screen
3. Click on the repository named Redeployment-Process

![repositories](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/01.repository-redeployment-process.PNG)

4. Once in the repository select the green icon GitPod to open the code on GitPod

![open-code-gitpod](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/02.open-code-gitpod.PNG)

5. Gitpod will load
6. The Redeployment Process Main branch will open
7. The Redeployment Process folders and files will be visible on the left hand side

![redeployment-process-files](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/03.redeployment-process-files.PNG)

8.The python file will be at the top level and is called:

* run.py - python code for the application
	
9. The credentials file creds.json has been added to gitignore as it contains sensitive information. This file will need to be saved again to the repository
		
10. Open the run.py file to amend or add to the python code

11. Make the required changes

![changes](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/04.amend-code.PNG)

12. Select Cntrl S to save changes (the white dot against the tab in which the code was changed will now disappear)

13. In the terminal type in "python3 run.py" and
press enter

![python3](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/05.python3.PNG)


15. The application will open in the command line. Run through the relevant action to which the changes were made. Test that the application is working as expected.

![view-changes](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/06.view-changes.PNG)

16. To save the changes back to github the following process needs to be followed:

* clear the terminal by typing in "clear" and pressing enter

* Add the code to gitpod by typing in "git add ." in terminal and press enter

![git-add](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/07.git-add.PNG)

* Commit the code to gitpod by typing in "git commit -m "Add a short message here" and press enter

![git-commit](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/08.git-commit.PNG)

* Push the code back down to github by typing in "git push" select enter

![git-push](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/09.git-push.PNG)

* From the github side, refresh the repository page and the commit will reflect

![change-github](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/10.new-commit.PNG)

* Open the item to view the commit changes

![commit](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/11.new-commit-details.PNG)

			
## Page Deployment

The website was deployed from GitHub to Heroku using the following steps:

1. Make sure that all input fields within the code have a new line captured at the end of the string:

![new-line](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/01.add-new-line.PNG)

This is due to an odd quirk in the software  Code Institute used to create the mock terminal.  
Without this extra line, the text for the import request will not show up in the terminal.   

2. A list of requirements create that the application needs to run must be created next.
This is a list of dependencies that the application requires to run that should be added to Heroku. Make sure you have a requirements.txt file saved in your repository. When you enter the below instruction you need to ensure that the file name matches exactly.

To create this list type 'pip3 freeze > requirements.txt' in the terminal and press enter

![pip-3](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/02.requirements-pip.PNG)

The requirements will now be added to the requirements.txt file

![requirements](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/03.requirements-document.PNG)

3. Commit and push these changes to GitHub

![commit-push](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/04.git-commit-push.PNG)

4. Go to Heroku - https://id.heroku.com/login and login or follow the steps to create a new account if necessary

5. From the Heroku dashboard click new and select create new app to create a new web application

![new](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/05.heroku-new.PNG)

6. Complete the app name and region fields and select create app

![create-app](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/06.create-app.PNG)

7. The page that is created contains everything you need to deploy the app. First access the settings tab

![settings](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/07.settings.PNG)

8. The first section to look at is the config vars. Click to open it

![config-vars](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/08.config-vars.PNG)

In the field for key enter CREDS

![creds](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/09.creds.PNG)

Go back to your workspace and copy the entire content of the creds.json file

Paste it into the value field and click add

![value-add](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/10.value-add.PNG)

9. The next step is to add a couple of build packs to the application. Click Add Buildpack

![buildpacks](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/11.buildpacks.PNG)

10. Select the buildpack python and click save changes

![buildpack-python](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/12.buildpack-python.PNG)

11. Select the buildpack nodejs and click save changes

![buildpack-nodejs](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/13.buildpack-nodejs.PNG)

12. Make sure that your buildpacks are in this order with python on top and nodejs underneath

![buildpacks-order](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/14.buildpacks-order.PNG)

13. Next click on the Deploy tab to go to the deploy section

Select your deployment method as GitHub by clicking on GitHub

![deployment-section](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/15.deploy-section.PNG)

14. Confirm connection to GitHub and then search for the depository name

![connect-github](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/16.connect-github.PNG)

15. Click connect to link up your github repository code

![connect-repository](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/17.connect-repository.PNG)

16. Select whether to deploy the app automatically or manually. I have selected automatically

![automatic-or-manual](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/18.automatic-or-manual.PNG)

17. Automatic deploys are now enabled from my main branch

![automatic-deploys](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/19.automatic-deploys.PNG)

18. To create an app now and not wait for a push click to manually deploy the main branch

![manually-deploy](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/20.manual-deploy.PNG)

19. The app will then be created

![app-creating](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/21.app-creating.PNG)

20. Once completed click on view to access the deployed site link

![view-access-link](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/heroku-deployment/22.view-access-link.PNG)


## How to Fork the Repository

1. To be able to fork the repository, you will need your own github and gitpod accounts with linked permissions

![updated-permissions](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/fork-repository/updated-permissions.png)

2. From your github home page in the search bar search for Claire-Potter
3. Under Users select the user Claire-Potter

![user-claire-potter](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/fork-repository/01.user-claire-potter.png)
4. On the repository page choose to open the Redeployment Process repository

![repositories](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/maintenance/01.repository-redeployment-process.PNG)

5. At the top of the page on the right-hand side select to Fork the repository

![fork-own-copy](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/fork-repository/02.fork-own-copy.PNG)

6. Your own version of the repository will create

![own-version](https://github.com/Claire-Potter/Redeployment-Process/blob/main/read-me-content/deployment/fork-repository/03.own-copy.PNG)

7. Select the green GitPod icon to open the work space on GitPod
8. Follow the steps in the Maintaining Code section above to make and save changes to your own repository
9. Remember you will need to create your own version of the cred.json file for the credentials to access the API.


# References

## Code

### General Queries

The following were used for any general queries or guidance required:

1. Code Institute LMS
2. Stack Overflow - https://stackoverflow.com/

### Code Adaptations

1. Function get_employee_number()
   This function was created based on the get_sales_data() function created in the Code Institute Love Sandwiches project. It has been adjusted to align with this application's requirements.
   
2. Function validate_number(value)
   This function was created based on the validate_data(values) function created in the Code Institute Love Sandwiches project. It has been adjusted to align with this application's requirements.
   
3. Function validate_date(my_str_date)
   The following article was referenced to convert to date:
   https://stackoverflow.com/questions/52260789/update-googlesheet-cell-with-timestamp-from-python
   
4. Function update_sheet(data, worksheet)
   This function was created based on the update_worksheet() function created in the Code Institute Love Sandwiches project. It has been adjusted to align with this application's requirements.
   
5. Function add_employee()
   The following article was referenced to return a cell's address:
   https://github.com/burnash/gspread/issues/41
   
6. Function select_field()
   the list.extend function was used as per
   the stackoverflow post:
   https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python/20196202
   
 7. Function update_single_cell(emp_value,    worksheet, column_value, change_value)
    the following article was referenced
    to update a single cell value:
    https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell  
    The following article was referenced to return a cell's address:
    https://github.com/burnash/gspread/issues/41
    
 8. Function fetch_current_salary(worksheet, emp_value, column_value)
    the following article was referenced to
    locate data using cell coordinates:
    https://www.makeuseof.com/tag/read-write-google-sheets-python/
    The following article was referenced to return a cell's address:
    https://github.com/burnash/gspread/issues/41
    
9. Function update_exit_date_status(worksheet, worksheet_two, emp_value, status_value)
   the following article was referenced
   to update a single cell value:
   https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell4  
   The following article was referenced to return a cell's address:
   https://github.com/burnash/gspread/issues/41  
   The following article was referenced to convert to date:
   https://stackoverflow.com/questions/52260789/update-googlesheet-cell-with-timestamp-from-python
   
 10. Function days_in_pool(worksheet, emp_value)
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
     
  11. Function place_employee()
      to access specific cell and return the value from the dataframe:
      https://pythonhow.com/accessing-dataframe-columns-rows-and-cells/
  
 12. Function retrench_employee()
     to access specific cell and return the value
     from the dataframe:
     https://pythonhow.com/accessing-dataframe-columns-rows-and-cells/  
     The following article was referenced to locate data using cell coordinates:
     https://www.makeuseof.com/tag/read-write-google-sheets-python/
     The following article was referenced to return a cell's address:
     https://github.com/burnash/gspread/issues/41
 
13. Function display_remove_rows(worksheet, sort_by, columns_list)
    The following article was referenced to create the .loc code:
    https://re-thought.com/how-to-change-or-update-a-cell-value-in-python-pandas-dataframe/  
    The following article was referenced for dataframe formatting:
    https://mode.com/example-gallery/python_dataframe_styling/  
    The following article was referenced to hide columns and index:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.hide_columns.html#pandas.io.formats.style.Styler.hide_columns
    
14. display_redeployment_pool(worksheet, sort_by, columns_list)
    The following article was referenced for dataframe formatting:
    https://mode.com/example-gallery/python_dataframe_styling/  
    The following article was referenced to hide columns and index:
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.hide_columns.html#pandas.io.formats.style.Styler.hide_columns


## Content

All of the written content was written by me.
The Redeployment Process was designed by me.

The mockup image in the ReadMe was created using the following site:
	* http://techsini.com/multi-mockup/index.php

# Acknowledgments

A huge thank you to my mentor Brian Macharia. The guidance and advice that you have provided has been invaluable.

Thank you so much to the Code Institute Tutoring Team as well as the Code Development Team who created a new Python Repository Template for me to utilise to deploy my site. I greatly appreciate your fantastic support.

Thank you to Code Institute for providing such well-thought out and put together course material and for the constant guidance and advice provided through Slack.

Finally, to my wonderful husband and children, thank you for your understanding and support through this process.
