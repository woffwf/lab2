from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.bll.models import Base, Candidate, Company, Vacancy, Application, Review
from app.bll.database import get_db
from pathlib import Path
import csv

app = FastAPI()

DATABASE_URL = "sqlite:///recruiting_app.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/import_data/")
def import_data(db: Session = Depends(get_db)):
    import_order = [
        ("candidates.csv", Candidate),
        ("companies.csv", Company),
        ("vacancies.csv", Vacancy),
        ("applications.csv", Application),
        ("reviews.csv", Review),
    ]
    results = {}
    try:
        for filename, model in import_order:
            path = Path(__file__).parent.parent / "data" / filename
            if not path.exists():
                raise HTTPException(400, detail=f"Файл {filename} не знайдено")

            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                objects = [model(**row) for row in reader]
                db.bulk_save_objects(objects)
                db.commit()
                results[filename] = len(objects)

        return {"message": "Дані імпортовано", "imported": results}
    except Exception as e:
        db.rollback()
        raise HTTPException(504, detail=f"Помилка імпорту: {str(e)}")

@app.get("/vacancies/")
def get_all_vacancies(db: Session = Depends(get_db)):
    try:
        return {"vacancies": db.query(Vacancy).all()}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/vacancies/{vacancy_id}")
def get_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    try:
        vacancy = db.query(Vacancy).filter(Vacancy.id == vacancy_id).first()
        if not vacancy:
            raise HTTPException(404, detail="Вакансія не знайдена")
        return {"vacancy": vacancy}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/companies/")
def get_all_companies(db: Session = Depends(get_db)):
    try:
        return {"companies": db.query(Company).all()}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/companies/{company_id}")
def get_company(company_id: int, db: Session = Depends(get_db)):
    try:
        company = db.query(Company).filter(Company.id == company_id).first()
        if not company:
            raise HTTPException(404, detail="Компанію не знайдено")
        return {"company": company}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/candidates/")
def get_all_candidates(db: Session = Depends(get_db)):
    try:
        return {"candidates": db.query(Candidate).all()}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    try:
        candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
        if not candidate:
            raise HTTPException(404, detail="Кандидат не знайдений")
        return {"candidate": candidate}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/applications/")
def get_all_applications(db: Session = Depends(get_db)):
    try:
        return {"applications": db.query(Application).all()}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/reviews/")
def get_all_reviews(db: Session = Depends(get_db)):
    try:
        return {"reviews": db.query(Review).all()}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/reviews/{review_id}")
def get_review(review_id: int, db: Session = Depends(get_db)):
    try:
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            raise HTTPException(404, detail="Відгук не знайдено")
        return {"review": review}
    except Exception as e:
        raise HTTPException(504, detail=str(e))

@app.get("/candidates/{candidate_id}/applications")
def get_candidate_applications(candidate_id: int, db: Session = Depends(get_db)):
    try:
        applications = db.query(Application).filter(Application.candidate_id == candidate_id).all()
        return {"applications": applications}
    except Exception as e:
        raise HTTPException(504, detail=str(e))
