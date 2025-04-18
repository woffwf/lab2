from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Candidate, Company, Vacancy, Application, Review

class ICandidateService(ABC):
    @abstractmethod
    def get_all_candidates(self) -> List[Candidate]:
        pass

    @abstractmethod
    def get_candidate_by_id(self, candidate_id: int) -> Optional[Candidate]:
        pass

class ICompanyService(ABC):
    @abstractmethod
    def get_all_companies(self) -> List[Company]:
        pass

    @abstractmethod
    def get_company_by_id(self, company_id: int) -> Optional[Company]:
        pass

class IVacancyService(ABC):
    @abstractmethod
    def get_all_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def get_vacancy_by_id(self, vacancy_id: int) -> Optional[Vacancy]:
        pass

class IApplicationService(ABC):
    @abstractmethod
    def get_applications_by_candidate(self, candidate_id: int) -> List[Application]:
        pass

class IReviewService(ABC):
    @abstractmethod
    def get_reviews_by_vacancy(self, vacancy_id: int) -> List[Review]:
        pass
