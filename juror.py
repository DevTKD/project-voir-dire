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
    military_status: str
    prior_jury_service: str

class EnhancedProfile:
    pass