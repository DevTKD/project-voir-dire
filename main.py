# main.py - Prevail Analytics | Caldwell v. Northbridge Medical Center
from juror import BasicProfile
from case import CaseProfile, CaseQuestion, RetainingParty
from evaluation import Evaluation
from scorer import juror_score

# --- CASE SETUP ---
# Caldwell v. Northbridge Medical Center
# Medical malpractice - defense retained Prevail Analytics
caldwell_case = CaseProfile(
    case_type="medical_malpractice",
    jurisdiction="Cook County",
    retained_by= RetainingParty.DEFENSE,
    questions=[
        CaseQuestion(field="trust_in_doctors", trigger_answer="low", weight=-30),
        CaseQuestion(field="personal_medical_injury", trigger_answer="yes", weight=-25),
        CaseQuestion(field="family_medical_injury", trigger_answer="yes", weight=-20),
        CaseQuestion(field="filed_lawsuit_before", trigger_answer="yes", weight=-20),
        CaseQuestion(field="trust_in_hospitals", trigger_answer="low", weight=-25),
        CaseQuestion(field="believes_doctors_overworked", trigger_answer="yes", weight=10),
    ]
)

# --- JUROR PROFILES ---
juror1 = BasicProfile(
    age_range="45-54",
    gender="female",
    marital_status="widowed",
    num_of_children=3,
    education_level="some_college",
    occupation="home_health_aide",
    employment_status="employed",
    income_range="30k-40k",
    homeownership_status="renter",
    military_status=False,
    prior_jury_service=True
)

juror2 = BasicProfile(
    age_range="35-44",
    gender="male",
    marital_status="married",
    num_of_children=0,
    education_level="graduate_degree",
    occupation="physician",
    employment_status="employed",
    income_range="200k+",
    homeownership_status="owner",
    military_status=False,
    prior_jury_service=False
)

# --- JUROR ANSWERS ---
juror1_answers = {
    "trust_in_doctors": "low",
    "personal_medical_injury": "yes",
    "family_medical_injury": "yes",
    "filed_lawsuit_before": "no",
    "trust_in_hospitals": "low",
    "believes_doctors_overworked": "no"
}

juror2_answers = {
    "trust_in_doctors": "high",
    "personal_medical_injury": "no",
    "family_medical_injury": "no",
    "filed_lawsuit_before": "no",
    "trust_in_hospitals": "high",
    "believes_doctors_overworked": "yes"
}

# --- SCORE BAR ---
def display_score_bar(score, min_score= 0, max_score=100):
    bar_length = 58
    normalized = (score - min_score) / (max_score - min_score)
    filled = int(normalized * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n  Score: {score} / 100")
    print(f"  [{bar}]")
    print(f"   Defense{'':<18}Neutral{'':<18}Plaintiff")

# --- SCORE BREAKDOWN ---
def display_breakdown(evaluation):
    print("\n  Score Breakdown:")
    for question in evaluation.case.questions:
        answer = evaluation.answers.get(question.field, "not answered")
        if answer == question.trigger_answer:
            result = f"{question.weight:+d} ← triggered"
        else:
            result = "no match"
        print(f"    {question.field}: {answer} → {result}")

# --- RUN EVALUATIONS ---
print("=" * 60)
print("  PREVAIL ANALYTICS")
print("  Case: Caldwell v. Northbridge Medical Center")
print(f"  Type: Medical Malpractice | Retained By: Defense")
print("=" * 60)

for juror, answers in [(juror1, juror1_answers), (juror2, juror2_answers)]:
    evaluation = Evaluation(juror=juror, case=caldwell_case, answers=answers)
    score = juror_score(evaluation)
    print(f"\n  Juror: {juror.occupation} | {juror.age_range} | {juror.gender}")
    display_breakdown(evaluation)
    display_score_bar(score)
    print()

print("=" * 60)