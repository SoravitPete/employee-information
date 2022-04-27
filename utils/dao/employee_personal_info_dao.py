from models.employee_personal_info_models import EmployeeInfo
from sqlalchemy.orm.session import Session


class EmployeeInfoDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_employee(self):
        return self.__session.query(EmployeeInfo).all()

    def get_employee_by_id(self, person_id):
        return self.__session.query(EmployeeInfo).filter(EmployeeInfo.person_id == person_id)[0]

    def get_employee_by_contract(self, contract):
        return self.__session.query(EmployeeInfo).filter(EmployeeInfo.contract == contract).all()

    def get_employee_by_city(self, city):
        return self.__session.query(EmployeeInfo).filter(EmployeeInfo.city == city).all()

    def get_employee_by_street(self, street):
        return self.__session.query(EmployeeInfo).filter(EmployeeInfo.street == street).all()

    def create_new_employee(self, employee: EmployeeInfo):
        self.__session.add(employee)
        self.__session.commit()
        print("add new element.")