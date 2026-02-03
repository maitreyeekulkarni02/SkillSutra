
def generate_feedback(answers):
    score = 0
    for ans in answers:
        if len(ans) > 20:
            score += 10

    feedback = {
        "communication": "Good" if score > 20 else "Needs Improvement",
        "confidence": "Average",
        "technical_depth": "Moderate"
    }

    return score, feedback
