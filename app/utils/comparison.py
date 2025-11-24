# app/utils/comparison.py
import json
import math
from typing import Optional, Dict, Tuple, List

# Path to your uploaded dataset (local)
DATA_PATH = "app/data/careers.json"

def load_careers() -> list:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

CAREERS = load_careers()

def find_career_by_name(name: str) -> Optional[dict]:
    n = name.strip().lower()
    for c in CAREERS:
        if c.get("career_name","").strip().lower() == n:
            return c
    # fuzzy fallback: check if name token appears in career_name
    for c in CAREERS:
        if n in c.get("career_name","").strip().lower():
            return c
    return None

def salary_midpoint(salary_str: str) -> float:
    """
    Parse strings like "3–40 LPA" or "3-40 LPA" or "30k-50k" etc.
    Returns midpoint numeric in the same units (we assume LPA is units).
    If parse fails, return 0.0
    """
    if not salary_str:
        return 0.0
    s = salary_str.replace("–", "-").replace("—","-")
    # remove non-digit except dot and hyphen
    # Try to extract two numbers
    import re
    nums = re.findall(r"[\d]+(?:\.\d+)?", s)
    if len(nums) >= 2:
        try:
            lo = float(nums[0])
            hi = float(nums[1])
            # Heuristic: if numbers look like thousands (e.g., >1000) we won't convert
            return (lo + hi) / 2.0
        except:
            return 0.0
    # fallback single number
    if len(nums) == 1:
        try:
            return float(nums[0])
        except:
            return 0.0
    return 0.0

def normalize_demand(text: str) -> float:
    if not text:
        return 0.5
    t = text.strip().lower()
    if "high" in t:
        return 1.0
    if "medium" in t:
        return 0.6
    if "low" in t:
        return 0.3
    # default / unknown
    return 0.5

def difficulty_rank(text: str) -> int:
    t = (text or "").strip().lower()
    if "easy" in t:
        return 1
    if "medium" in t:
        return 2
    if "hard" in t:
        return 3
    return 2

def overlap_score(list1: List[str], list2: List[str]) -> float:
    s1 = set([x.strip().lower() for x in list1])
    s2 = set([x.strip().lower() for x in list2])
    if not s1 and not s2:
        return 0.0
    inter = s1.intersection(s2)
    union = s1.union(s2)
    score = (len(inter) / max(1, len(union))) * 100.0
    return round(score, 2)

def build_summary(c: dict) -> Dict:
    required = c.get("required_skills", []) or []
    optional = c.get("optional_skills", []) or []
    return {
        "career_name": c.get("career_name", ""),
        "difficulty": c.get("difficulty_level", ""),
        "salary_midpoint": salary_midpoint(c.get("salary_range","")),
        "demand_level": c.get("demand_level", ""),
        "required_skills": required,
        "optional_skills": optional
    }

def compare_careers(name1: str, name2: str, prefer: Optional[str]=None) -> dict:
    c1 = find_career_by_name(name1)
    c2 = find_career_by_name(name2)

    if not c1 or not c2:
        return {"error": "one_or_both_not_found", "career_1": c1, "career_2": c2}

    s1 = build_summary(c1)
    s2 = build_summary(c2)

    # Skills
    req1 = s1["required_skills"]
    req2 = s2["required_skills"]
    shared = sorted(list(set([x.lower() for x in req1]) & set([x.lower() for x in req2])))
    unique1 = sorted(list(set([x.lower() for x in req1]) - set([x.lower() for x in req2])))
    unique2 = sorted(list(set([x.lower() for x in req2]) - set([x.lower() for x in req1])))

    # Overlap %
    overlap = overlap_score(req1 + s1["optional_skills"], req2 + s2["optional_skills"])

    # Which is easier? Use difficulty_rank and count of required skills length as tiebreaker
    dr1 = difficulty_rank(s1["difficulty"])
    dr2 = difficulty_rank(s2["difficulty"])
    if dr1 < dr2:
        easier = s1["career_name"]
    elif dr2 < dr1:
        easier = s2["career_name"]
    else:
        # tiebreak by fewer required_skills
        if len(req1) < len(req2):
            easier = s1["career_name"]
        elif len(req2) < len(req1):
            easier = s2["career_name"]
        else:
            easier = "Comparable"

    # Demand
    d1 = normalize_demand(s1["demand_level"])
    d2 = normalize_demand(s2["demand_level"])
    if d1 > d2:
        more_demand = s1["career_name"]
    elif d2 > d1:
        more_demand = s2["career_name"]
    else:
        more_demand = "Comparable"

    # Salary difference (midpoints)
    sal1 = s1["salary_midpoint"]
    sal2 = s2["salary_midpoint"]
    sal_diff = round(sal1 - sal2, 2)

    # Build recommendation text (short AI judge)
    rec = []
    # Basic rule-based recommendation considering prefer
    if prefer:
        p = prefer.lower()
        if "salary" in p:
            if sal1 > sal2:
                rec.append(f"If you prioritise salary, choose {s1['career_name']}.")
            elif sal2 > sal1:
                rec.append(f"If you prioritise salary, choose {s2['career_name']}.")
            else:
                rec.append("Salaries are similar for both careers.")
        elif "ease" in p or "easy" in p or "difficulty" in p:
            rec.append(f"If you prefer easier learning curve, {easier} is the better choice.")
        elif "growth" in p or "demand" in p:
            if d1 > d2:
                rec.append(f"{s1['career_name']} shows higher demand.")
            elif d2 > d1:
                rec.append(f"{s2['career_name']} shows higher demand.")
            else:
                rec.append("Demand looks comparable.")
    else:
        # Generic recommendation: weigh demand + salary + overlap
        score1 = (d1 * 0.5) + (min(sal1/50.0,1.0)*0.3) + ( (len(shared)/max(1,len(req1))) * 0.2 )
        score2 = (d2 * 0.5) + (min(sal2/50.0,1.0)*0.3) + ( (len(shared)/max(1,len(req2))) * 0.2 )
        if score1 > score2:
            rec.append(f"Overall, {s1['career_name']} scores higher based on demand & salary normalization.")
        elif score2 > score1:
            rec.append(f"Overall, {s2['career_name']} scores higher based on demand & salary normalization.")
        else:
            rec.append("Both careers are close matches; choose by personal interest.")

    explanation = (
        f"I compared difficulty, salary midpoint, demand level, and required skills overlap. "
        f"{s1['career_name']} midpoint salary: {sal1}. {s2['career_name']} midpoint salary: {sal2}. "
        f"Shared skills: {', '.join(shared) if shared else 'none'}."
    )

    return {
        "career_1": s1,
        "career_2": s2,
        "comparison": {
            "which_is_easier": easier,
            "which_has_more_demand": more_demand,
            "salary_difference": sal_diff,
            "overlap_score": overlap,
            "shared_skills": shared,
            "unique_to_career_1": unique1,
            "unique_to_career_2": unique2,
            "recommendation": " ".join(rec),
            "explanation": explanation
        }
    }
