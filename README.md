# Machine Learning Powered Crop Recommendation"

📘 Overview

The Crop Recommendation System is a Flask-based machine learning web application that recommends the most suitable crop to cultivate based on environmental and soil parameters.
By leveraging agricultural data and machine learning algorithms, this project helps farmers and researchers make data-driven decisions to improve productivity and sustainability.

🖥️ Project Demo
<img src="https://github.com/<your-username>/Machine-Learning-Crop-Recommendation/blob/main/static/demo.png" width="400"/>

🟢 Sample Output:
Recommended Crop: banana

🚀 Features

✅ Predicts the most suitable crop based on soil and weather conditions
✅ Simple and responsive Flask web interface
✅ Accepts user input for essential agricultural parameters
✅ Displays clear and instant crop recommendations
✅ Trained on real-world agricultural dataset

🧠 Technologies Used

Programming Language: Python

Framework: Flask

Libraries & Tools:

Pandas

NumPy

Scikit-learn

Matplotlib / Seaborn

Pickle

HTML, CSS (for UI)

Dataset: Crop Recommendation Dataset (Kaggle)

📂 Project Structure
📦 Crop-Recommendation
├── app.py                     # Main Flask application
├── model/
│   └── crop_model.pkl         # Trained ML model
├── templates/
│   └── index.html             # Frontend HTML page
├── static/
│   ├── style.css              # Styling for UI
│   └── demo.png               # Screenshot or sample output
├── dataset/
│   └── Crop_recommendation.csv
├── notebooks/
│   └── EDA_and_Model.ipynb    # Jupyter notebook for training
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Machine-Learning-Crop-Recommendation.git
cd Machine-Learning-Crop-Recommendation

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Flask Application
python app.py

4️⃣ Open in Browser

Go to: 👉 http://127.0.0.1:5000/

🌱 Input Parameters
Feature	Description
Nitrogen (N)	Nitrogen content in soil
Phosphorus (P)	Phosphorus content in soil
Potassium (K)	Potassium content in soil
Temperature (°C)	Temperature of the area
Humidity (%)	Humidity in the air
pH	Acidity or alkalinity of soil
Rainfall (mm)	Average rainfall in millimeters
🧾 Example Output

Input:

N = 90, P = 42, K = 43, Temperature = 25°C, Humidity = 80%, pH = 6.5, Rainfall = 200 mm


Predicted Crop: 🌾 Banana

📈 Model Performance
Algorithm	Accuracy
Random Forest Classifier	98%
Decision Tree Classifier	95%
SVM	93%

The Random Forest model was selected for final deployment.

💡 Future Enhancements

🌦️ Integration with live weather APIs for dynamic recommendations

📱 Mobile-friendly dashboard or Android app

🧬 Add soil quality and fertilizer suggestions

🔊 Voice assistant for accessibility

🤝 Contribution

Contributions are always welcome!

Fork this repository

Create your branch: git checkout -b feature-branch

Commit changes: git commit -m "Added new feature"

Push the branch: git push origin feature-branch

Submit a Pull Request

🧑‍💻 Author

Praveen G
📧 [your-email@example.com
]
🔗 LinkedIn Profile

💻 Passionate about AI, Data Science & Smart Agriculture

🪪 License

This project is licensed under the MIT License – you’re free to use, modify, and distribute it.
