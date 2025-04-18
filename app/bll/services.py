from sqlalchemy.orm import Session
from .dal import CandidateDAL, CompanyDAL, VacancyDAL, ApplicationDAL, ReviewDAL
from .interfaces import ICandidateService, ICompanyService, IVacancyService, IApplicationService, IReviewService

class CandidateService(ICandidateService):
    def __init__(self, db: Session):
        self.dal = CandidateDAL(db)

    def get_all_candidates(self):
        return self.dal.get_all_candidates()

    def get_candidate_by_id(self, candidate_id: int):
        return self.dal.get_candidate_by_id(candidate_id)

class CompanyService(ICompanyService):
    def __init__(self, db: Session):
        self.dal = CompanyDAL(db)

    def get_all_companies(self):
        return self.dal.get_all_companies()

    def get_company_by_id(self, company_id: int):
        return self.dal.get_company_by_id(company_id)

class VacancyService(IVacancyService):
    def __init__(self, db: Session):
        self.dal = VacancyDAL(db)

    def get_all_vacancies(self):
        return self.dal.get_all_vacancies()

    def get_vacancy_by_id(self, vacancy_id: int):
        return self.dal.get_vacancy_by_id(vacancy_id)

class ApplicationService(IApplicationService):
    def __init__(self, db: Session):
        self.dal = ApplicationDAL(db)

    def get_applications_by_candidate(self, candidate_id: int):
        return self.dal.get_applications_by_candidate(candidate_id)

class ReviewService(IReviewService):
    def __init__(self, db: Session):
        self.dal = ReviewDAL(db)

    def get_reviews_by_vacancy(self, vacancy_id: int):
        return self.dal.get_reviews_by_vacancy(vacancy_id)
