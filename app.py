from flask import Flask, render_template, request
import os
import pickle
import numpy as np

app = Flask(__name__)

# Lazy-load the trained model using an absolute path (safer for serverless)
_model = None

def get_model():
    global _model
    if _model is not None:
        return _model
    # Resolve model path relative to this file, or via env var MODEL_PATH
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.environ.get('MODEL_PATH', os.path.join(base_dir, 'model.pkl'))
    with open(model_path, 'rb') as f:
        _model = pickle.load(f)
    return _model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from the HTML form
        nitrogen = float(request.form['Nitrogen'])
        phosphorus = float(request.form['Phosphorus'])
        potassium = float(request.form['Potassium'])
        temperature = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        # Prepare input as a 2D array for model
        features = np.array([[nitrogen, phosphorus, potassium,
                              temperature, humidity, ph, rainfall]], dtype=float)

        # Make prediction
        model = get_model()
        prediction = model.predict(features)[0]   # e.g. crop name

        return render_template('index.html',
                               prediction_text=f"Recommended Crop: {prediction}")

    except Exception as e:
        # For production, avoid leaking internals; optionally log e
        return render_template('index.html',
                               prediction_text="⚠️ Error: Please enter valid inputs.")

if __name__ == '__main__':
    app.run(debug=True)
