# This section defines the context in which jurors are evaluated

from dataclasses import dataclass
from enum import Enum

class RetainingParty(Enum):
    PLAINTIFF = "plaintiff"
    DEFENSE = "defense"

@dataclass
class CaseQuestion:
    field: str
    trigger_answer: str
    weight: int

@dataclass
class CaseProfile:
    case_type: str
    jurisdiction: str
    retained_by: RetainingParty
    questions: list[CaseQuestion]
