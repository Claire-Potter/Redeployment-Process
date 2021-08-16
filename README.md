# Redeployment Process

The redeployment process is utilised by a company undergoing change which results in certain positions becoming redundant. The application will be utilised to add affected employees to a redeployment pool, update employee details, place employees in new positions or retrench employees.

![redeployment-process-mockup](https://github.com/Claire-Potter/Redeployment-Process/blob/98c1262e8a1b196a85e1560c0cc525df2268e63a/read-me-content/mock-up-image.PNG)

<a href="https://redeployment-process.herokuapp.com/" target="_blank">Click Here</a> to access the site.

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
	  gspread
	  inquirer
	  pandas
	  datetime
	  IPython.display
	  
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

### Release One

#### Functional Requirements

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
14. The difference in salaries for placed candidates should be calculated.
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

## Surface

As this application is written in Python and displays within the command line, design aspects were minimal and provided for within the Code Institute template.

## Technologies

The process is coded in Python. The database is setup in google sheets. The following libraries are used to provide the necessary functionality:
	  gspread
	  inquirer
	  pandas
	  datetime
	  IPython.display
	  
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

# Deployment

## Development Interface

This website was developed on Gitpod using the Code Institute Python student template with changes frequently committed to git then pushed onto GitHub from the Gitpod terminal.

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
   
5. Function add_candidate()
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
     
  11. Function place_candidate()
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

Thank you to Code Institute for providing such well-thought out and put together course material and for the constant guidance and advice provided through Slack.

Finally, to my wonderful husband and children, thank you for your understanding and support through this process.
