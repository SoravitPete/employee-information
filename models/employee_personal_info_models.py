from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class EmployeeInfo(Base):
    __tablename__ = "employee_personal_info"

    person_id = Column(Integer, primary_key=True, nullable=False)
    gender = Column(Text, nullable=False)
    contract = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    street = Column(Text, nullable=False)
    education = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Employee info: (person_id={self.person_id},gender={self.gender},contract={self.contract}," \
               f"city={self.city},street={self.street},education={self.education})>"