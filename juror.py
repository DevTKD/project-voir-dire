# Hold the juror profiles: basic and enhanced
from dataclasses import dataclass

@dataclass
class BasicProfile:
    age_range: str
    gender: str
    marital_status: str
    num_of_children: int
    education_level: str
    occupation: str
    employment_status: str
    income_range: str
    homeownership_status: str
    military_status: bool
    prior_jury_service: bool

@dataclass
class EnhancedProfile:
    business_owner: str
    union_member: str
    prior_law_enforcement: str
    legal_professional: str
    government_employee: str
    prior_witness_experience: str
    