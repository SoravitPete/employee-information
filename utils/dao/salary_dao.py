from models.salary_models import Salary
from sqlalchemy.orm.session import Session


class SalaryDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_salary(self):
        return self.__session.query(Salary).all()

    def get_salary_by_id(self, person_id):
        return self.__session.query(Salary).filter(Salary.person_id == person_id)[0]