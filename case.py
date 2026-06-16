# This section defines the context in which jurors are evaluated

from dataclasses import dataclass

@dataclass
class CaseProfile:
    case_type: str
    jurisdiction: str
    questionnaire_fields: list

