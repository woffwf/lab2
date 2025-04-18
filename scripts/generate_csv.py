import csv
from faker import Faker
import random
from pathlib import Path

fake = Faker()
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def generate_test_data():
    with open(DATA_DIR / "candidates.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email"])
        for i in range(1, 201):
            writer.writerow([i, fake.name(), fake.email()])

    with open(DATA_DIR / "companies.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name"])
        for i in range(1, 6):
            writer.writerow([i, fake.company()])

    with open(DATA_DIR / "vacancies.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "description", "year", "company_id"])
        for i in range(1, 301):
            writer.writerow([
                i,
                fake.job(),
                fake.text(max_nb_chars=100),
                random.randint(2010, 2024),
                random.randint(1, 5)
            ])

    with open(DATA_DIR / "applications.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "candidate_id", "vacancy_id"])
        for i in range(1, 1001):
            writer.writerow([
                i,
                random.randint(1, 200),
                random.randint(1, 300)
            ])

    with open(DATA_DIR / "reviews.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "score", "comment", "candidate_id", "vacancy_id"])
        for i in range(1, 801):
            writer.writerow([
                i,
                random.randint(1, 5),
                random.choice(["Great", "Ok", "Not bad", "Bad"]),
                random.randint(1, 200),
                random.randint(1, 300)
            ])

if __name__ == "__main__":
    generate_test_data()
    print("Test data generated in data/")
