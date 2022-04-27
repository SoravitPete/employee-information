from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Salary(Base):

    __tablename__ = "states"
    person_id = Column(Integer, primary_key=True, nullable=False)
    person_first_name = Column(Text, nullable=False)
    person_last_name = Column(Text, nullable=False)
    salary = Column(Integer, nullable=False)


    def __repr__(self) -> str:
        return f"<Salary: (person_id={self.person_id},firstname={self.person_first_name},lastname={self.person_last_name}" \
               f"salary={self.salary})>"