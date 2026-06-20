from flask import Flask
from flask import request
from flask import jsonify

from rag import get_answer

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error": "Invalid JSON"
            }), 400

        question = data.get("question")

        if not question:

            return jsonify({
                "error": "Question cannot be empty"
            }), 400

        answer = get_answer(question)

        return jsonify({
            "answer": answer
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)