# Redeployment Process

The redeployment process is utilised by a company undergoing change which results in certain positions becoming redundant. The process will be utilised to add affected employees to a redeployment pool, update employee details, place employees in new positions or retrench employees.

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
17. All data captured should be consolidated and added to the placed candidates sheet within the workbook.
18. The relevant fields within the redeployment pool should be updated with the new data.
19. The user should be able to action a retrenchment.
20. The user should be able to select an employee from within the redeployment pool to retrench.
21. This employee cannot have the status placed or retrenched already.
22. Once the employee is selected, the retrenchment package should be calculated utilising information from within the redeployment pool.
23. The data should be consolidated and saved to the retrenched candidates sheet within the workbook.
24. The user should be able to view the data available in google sheets via the console.


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

  - The content is coded in python and thus displays within the console. This is because it is a back-end language utilised to collect data and accurately update the database.
 - As a user begins the process, they will first encounter the main menu which provides them with the option to perform the four actions, view the data tables or exit the process. 
 - The first action will allow them to add a user to the redeployment pool. It logically goes through the fields, asking for the correct data and validating before consolidating and adding it back to the redeployment pool. Once complete the user will be taken back to the main menu. 
 - The second action will allow the user to update an employee within the redeployment pool. It only displays employees who are active within the pool, as once they are placed or retrenched, their data should no longer be changed. The user has the choice to continue to update different fields or to return to the menu.
 - The third action allows the user to place the employee into a new position. This asks for new department, position and salary information and calculates the difference in salary. The user is asked each question in a logical order. Once again, only employees who are active within the pool can be selected. The user will be returned to the main menu when done.
 - The fourth action enables the user to retrench an employee. This will be performed by selecting an active employee, the function will then calculate the retrenchment package and add the information to the database. The user will be directed back to the main menu when done.
 - The next option on the main menu is to view data tables. This will take the user to a menu of tables to select from. These are labeled according to the data that they display and will print the table to the console. The setup is clear and simple to enable the user to view the necessary data clearly.
 - The final option is to exit the process which will exit the user from the redeployment process.

 4. Is the technology appropriate?  
	 
	 The process is coded in Python. The database is setup in google sheets. The following imports are used to provide the necessary functionality:
	 - gspread
	 - inquirer
	 - pandas
	 - datetime
	 - IPython.display
	 
The user will be able to access the process directly within the console.

### High-level Business Goals

 - Create a functional programme to accurately complete the various actions within the redeployment process.
 - Maintain the redeployment database within google sheets.
 - Add validated data to google sheets and return relevant data when requested.
 - Perform all calculations and return correct values.

### Value

The value of the redeployment process is that it allows the user to fully maintain the redeployment database.
This ensures that the employee data is accurate and can be fed to recruitment systems, payroll and the database can be utilised to create reports and dashboards.
As the database is updated as and when actions occur this provides the company with the ability to provide regular live updates on the redeployment process. It also allows the company to accurately track placement costs/savings, retrenchment costs and the ultimate value provided by the redeployment process. Additional to this, all data is validated ensuring accuracy and avoiding duplication.

### Trade-offs

Using the trade-off process to rank the importance and feasibility of the opportunities I have decided:

1. To go ahead with 10/13 of the opportunities.
2. I will not be creating a front end site to complete the process on as this is a minimum viable product.
3. This would be a future opportunity to explore.

![Table depicting the Importance rating vs. the Feasibility rating per Opportunity](https://github.com/Claire-Potter/redeployment-process/blob/main/read-me-content/trade-offs-table.PNG)
   

## Scope
To provide a redeployment process to be utilised to add affected employees to a redeployment pool, update employee details, place employees in new positions or retrench employees. To be able to update the google sheets database as well as return data when required.

### Feature Trade Off

 <a href="https://github.com/Claire-Potter/redeployment-process/blob/main/read-me-content/feature-trade-offs.PNG">Feature Trade Off Table</a>


This site will be developed as a minimum viable product. Future releases could include additional functionality depending on the success of the first release. This could be include a front-end website to complete the process on as well as generate the tables and data charts.
