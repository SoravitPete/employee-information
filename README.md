# employee-information
Application for company database
which is contain employee data

# Setups for project

1.Create employee.db for the Window,
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
```

Example of the data in this project.

**salary Table**
| person_id | person_first_name | person_last_name | salary | 
|----|-------------|--------|-----|
| 1 | Aiden | Redfern | 174345 |

**employee personal info Table**
| person_id | gender | contract | city | street | education |
|----|------------|------------|-----|-----|-----|
| 1 | Male | Chad_Weatcroft3093@nickia.com | Honolulu | Maple Tunnel | Corporate university |
