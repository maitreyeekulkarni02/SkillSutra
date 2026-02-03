import json

def get_questions(role):
    with open("data/questions.json") as f:
        questions = json.load(f)
    return questions.get(role, [])

