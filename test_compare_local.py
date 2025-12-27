# test_compare_local.py

from app.utils.data_loader import load_careers_json
from app.utils.comparison_engine import compare_two_careers

def run_test():
    careers = load_careers_json()

    # pick two careers from your dataset
    career_a = next(c for c in careers if c["career_name"] == "Data Scientist")
    career_b =next(c for c in careers if c["career_name"] == "Data Analyst")

    result = compare_two_careers(
        career_a=career_a,
        career_b=career_b,
        user_skills=["Python", "SQL"],
        interest="data",
        effort=3
    )

    print("\n=== COMPARISON RESULT ===\n")
    print(result)

if __name__ == "__main__":
    run_test()
