from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message": "MigraCare API Running"}

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    score = 0
    triggers = []
    if data.get('sleep_hours',7) < 6:
        score+=30; triggers.append('Low Sleep')
    if data.get('stress_level',5) > 7:
        score+=25; triggers.append('High Stress')
    risk = "High" if score>=50 else "Low"
    return jsonify({"risk": risk, "score": score, "triggers": triggers})

@app.route('/api/diary', methods=['POST'])
def diary():
    return jsonify({"status": "saved", "entry": request.json})

if __name__ == '__main__':
    app.run(debug=True)
