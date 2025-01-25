from flask import Flask, request, jsonify

app = Flask(__name__)

symptoms_list = [
    "fever", "cough", "headache", "nausea", "chills", "dizziness",
    "fatigue", "vomiting", "diarrhea", "body ache", "sore throat", "rash"
]

def extract_symptoms(input_text, symptoms):
    detected_symptoms = []
    for symptom in symptoms:
        if symptom in input_text.lower():
            detected_symptoms.append(symptom)
    return detected_symptoms

@app.route('/')
def home():
    return "Welcome to the Symptom Extraction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_text = data.get('input_text', '')
    symptoms = extract_symptoms(input_text, symptoms_list)
    return jsonify({'symptoms': symptoms})

if __name__ == '__main__':
    app.run(debug=True)