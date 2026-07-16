# main.py - runs a sample juror evaluation for Prevail Analytics
from juror import BasicProfile
from case import CaseProfile, CaseQuestion
from evaluation import Evaluation
from scorer import juror_score

# create a sample juror
juror1 = BasicProfile(
    age_range="35-44",
    gender="male",
    marital_status="married",
    num_of_children=2,
    education_level="high_school",
    occupation="construction",
    employment_status="employed",
    income_range="40k-60k",
    homeownership_status="renter",
    military_status=False,
    prior_jury_service=False
)

# define a criminal case with scoring rules
criminal_case = CaseProfile(
    case_type="criminal",
    jurisdiction="Cook County",
    questions=[
        CaseQuestion(field="convicted_felon", trigger_answer="yes", weight=-20),
        CaseQuestion(field="law_enforcement_empathy", trigger_answer="no", weight=-25),
        CaseQuestion(field="prior_victim_of_crime", trigger_answer="yes", weight=15),
    ]
)

# juror's answers to case specific questions
juror1_answers = {
    "convicted_felon": "no",
    "law_enforcement_empathy": "no",
    "prior_victim_of_crime": "yes"
}

# run the evaluation
evaluation1 = Evaluation(juror=juror1, case=criminal_case, answers=juror1_answers)
score = juror_score(evaluation1)

print(f"Juror: {juror1.occupation}, {juror1.age_range}")
print(f"Case: {criminal_case.case_type} - {criminal_case.jurisdiction}")
print(f"Final Score: {score}")