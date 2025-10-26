# app.py
from flask import Flask, render_template, request
import joblib
import os


template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
app = Flask(__name__, template_folder=template_dir)

# Load your ML model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as f:
    model = joblib.load(f)
print("Model loaded successfully.")
print(type(model))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    inputs = [float(request.form.get(field)) for field in ['input1', 'input2', 'input3', 'input4', 'input5', 'input6', 'input7']]
    # Make prediction
    prediction = model.predict([inputs])
    crop_name = prediction[0]
    return render_template('result.html', crop=crop_name)

if __name__ == '__main__':
    app.run(debug=True)
