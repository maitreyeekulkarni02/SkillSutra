from flask import Flask, request, jsonify
from interview_engine import get_questions
from feedback import generate_feedback

app = Flask(__name__)

@app.route("/interview", methods=["POST"])
def interview():
    data = request.json
    role = data.get("role")
    answers = data.get("answers")

    score, feedback = generate_feedback(answers)
    return jsonify({
        "score": score,
        "feedback": feedback
    })

if __name__ == "__main__":
    app.run(debug=True)
