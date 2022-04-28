# employee-information
Application for company database
which is contain employee data

# Setups for project

1.Create employee.db
For the Window,
```
sqlite3 employee.db --init employee.schema
```
2.Open employee.db
```
sqlite3 employee.db
```
3.import csv file to employee.db
```
sqlite> .mode csv
sqlite> .import data/employee_personal_info.csv employee_personal_info
sqlite> .import data/salary.csv salary
