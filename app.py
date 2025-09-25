from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

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
                              temperature, humidity, ph, rainfall]])

        # Make prediction
        prediction = model.predict(features)[0]   # e.g. crop name

        return render_template('index.html',
                               prediction_text=f"Recommended Crop: {prediction}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text="⚠️ Error: Please enter valid inputs.")

if __name__ == '__main__':
    app.run(debug=True)
