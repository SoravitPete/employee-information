from utils.company_information import CompanyInfo

company_info = CompanyInfo()

print(company_info.employee().get_all_employee())
print(company_info.employee().get_employee_by_contract('Doug_Morris1167@dionrab.com'))
print(company_info.employee().get_employee_by_city("Atlanta"))
print(company_info.employee().get_employee_by_street("Blackheath  Road"))
print(company_info.salary().get_all_salary())
print(company_info.salary().get_salary_by_id(3))