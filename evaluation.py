# holds the relationship between the juror and case
from dataclasses import dataclass
from case import CaseProfile
from juror import BasicProfile

@dataclass
class Evaluation:
    juror: BasicProfile
    case: CaseProfile
    juror_score: int