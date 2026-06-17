# This section defines the context in which jurors are evaluated

from dataclasses import dataclass

@dataclass
class CaseQuestion:
    field: str
    trigger_answer: str
    weight: int

@dataclass
class CaseProfile:
    case_type: str
    jurisdiction: str
    questions: list[CaseQuestion]
