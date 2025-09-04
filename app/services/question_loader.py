import os,re
import pandas as pd

DATA_DIR = 'questions'

def extract_slug_from_url(url):
    match = re.search(r'/problems/([^/]+)/?', url)
    return match.group(1) if match else ""


def load_questions(company):
    filepath = os.path.join(DATA_DIR, f"{company}.csv")
    if not os.path.exists(filepath):
        return {"error": f"No data found for company {company}"}, 404

    df = pd.read_csv(filepath)
    questions = []
    for _, row in df.iterrows():
        questions.append({
            "Company": company,
            "Title": row.get("Title", ""),
            "Difficulty": row.get("Difficulty", ""),
            "Link": row.get("Link", ""),
            "Slug": extract_slug_from_url(row.get("Link", ""))
        })
    return questions

def get_companies_name():
    return [f[:-4] for f in os.listdir(DATA_DIR) if f.endswith(".csv")]