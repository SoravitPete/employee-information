from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.salary_dao import SalaryDao
from utils.dao.employee_personal_info_dao import EmployeeInfoDao

class CompanyInfo:


  def __init__(self, connection_url="sqlite:///employee.db"):
    engine = create_engine(connection_url)
    session = sessionmaker(bind=engine)
    self.__db_session = session()


  def employee(self):
    return EmployeeInfoDao(self.__db_session)

  def salary(self):
    return SalaryDao(self.__db_session)