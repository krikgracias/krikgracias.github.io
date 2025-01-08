from flask import Flask, request, jsonify
import io

app = Flask(__name__)

@app.route('/quiz', methods=['GET'])
def get_quiz():
    quiz = [
        {"id": 1, "prompt": "Write a function to add two numbers."},
        {"id": 2, "prompt": "Write a function to calculate the area of a rectangle."}
    ]
    return jsonify(quiz)

@app.route('/submit', methods=['POST'])
def submit_code():
    data = request.json
    user_code = data.get("code")
    try:
        # Execute user code
        stdout = io.StringIO()
        exec(user_code, {"__builtins__": {}}, {})
        output = stdout.getvalue()
        return jsonify({"success": True, "output": output})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
