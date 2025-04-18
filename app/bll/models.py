from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Vacancy(Base):
    __tablename__ = "vacancies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    year = Column(Integer)
    company_id = Column(Integer, ForeignKey("companies.id"))

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"))

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"))
