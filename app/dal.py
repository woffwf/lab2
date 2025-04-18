from sqlalchemy.orm import Session
from .models import Candidate, Company, Vacancy, Application, Review

class CandidateDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_all_candidates(self):
        return self.db.query(Candidate).all()

    def get_candidate_by_id(self, candidate_id: int):
        return self.db.query(Candidate).filter(Candidate.id == candidate_id).first()

class CompanyDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_all_companies(self):
        return self.db.query(Company).all()

    def get_company_by_id(self, company_id: int):
        return self.db.query(Company).filter(Company.id == company_id).first()

class VacancyDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_all_vacancies(self):
        return self.db.query(Vacancy).all()

    def get_vacancy_by_id(self, vacancy_id: int):
        return self.db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()

    def get_vacancies_by_company(self, company_id: int):
        return self.db.query(Vacancy).filter(Vacancy.company_id == company_id).all()

class ApplicationDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_applications_by_candidate(self, candidate_id: int):
        return self.db.query(Application).filter(Application.candidate_id == candidate_id).all()

    def get_applications_by_vacancy(self, vacancy_id: int):
        return self.db.query(Application).filter(Application.vacancy_id == vacancy_id).all()

class ReviewDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_reviews_by_candidate(self, candidate_id: int):
        return self.db.query(Review).filter(Review.candidate_id == candidate_id).all()

    def get_reviews_by_vacancy(self, vacancy_id: int):
        return self.db.query(Review).filter(Review.vacancy_id == vacancy_id).all()
