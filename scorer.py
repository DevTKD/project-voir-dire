# calculates a juror's score based on case questions and their answers
from evaluation import Evaluation

def juror_score(evaluation: Evaluation) -> int:
    total_score = 0
    for question in evaluation.case.questions:
        juror_answer = evaluation.answers.get(question.field)
        if juror_answer == question.trigger_answer:
            total_score += question.weight
    evaluation.juror_score = total_score
    return total_score