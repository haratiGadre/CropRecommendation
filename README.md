# 🌾 Crop Recommendation Web App

A Flask-based web application that predicts the most suitable crop to grow based on soil and environmental parameters using a Machine Learning model (Decision Tree Classifier).

This project combines Data Science, Machine Learning, and Web Development to create a real-world agricultural solution.

## 🚀 Features

- Predicts the best crop based on user inputs like N, P, K, temperature, humidity, pH, and rainfall.

- Simple and responsive web interface using HTML and CSS.

- Trained Decision Tree Classifier model for accurate predictions.

- Modular structure with separate frontend and backend folders.

## 🧠 Tech Stack

### **Languages & Frameworks**

- Python
- Flask
- HTML, CSS

### **Libraries**

- Pandas
- NumPy
- Scikit-learn
- Joblib

### **Tools**

- Google Colab
- VS Code
- Git & GitHub

## Folder Structure

```
CropRecommendationProject/
├── backend/
│   ├── index.py              # Flask application
│   ├── model.pkl             # Trained ML model
│   ├── classes.pkl           # Crop label classes
│
├── frontend/
│   ├── index.html            # Homepage
│   ├── prediction.html       # Input form page
│   └── result.html           # Result display page
│
├── mlModel/
│   └── Crop_Recommendation.csv  # Dataset
│
├── venv/                     # Virtual environment (for dependencies)
│   ├── Scripts/
│   ├── Lib/
│   └── Include/
│
├── requirements.txt          # List of required Python packages
└── README.md                 # Project documentation

```

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/CropRecommendationProject.git

cd CropRecommendationProject
```

### 2️⃣ Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv

venv\Scripts\activate     # For Windows
```

**OR**

```bash
source venv/bin/activate  # For Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

###4️⃣ Run the Flask App

```bash
cd backend

python index.py
```

### 5️⃣ Open in Browser

Go to:

👉 http://127.0.0.1:5000/

## 🧩 Input Parameters
| Input Field | Description |
|--------------|-------------|
| **N** | Nitrogen content in the soil (mg/kg) |
| **P** | Phosphorus content in the soil (mg/kg) |
| **K** | Potassium content in the soil (mg/kg) |
| **Temperature** | Temperature in °C |
| **Humidity** | Relative humidity in % |
| **pH** | Acidity or alkalinity of the soil |
| **Rainfall** | Average rainfall in mm |


## 📊 ML Model

**Algorithm:** Decision Tree Classifier

**Accuracy:** ~0.98 (on test data)

**Dataset:** Crop Recommendation Dataset

The model is trained using:

```python
 clf = DecisionTreeClassifier()

 clf.fit(X_train, y_train)

 joblib.dump(clf, 'backend/model.pkl')
```
## 💾 Example Workflow

- User enters soil and weather parameters.

- Flask backend passes data to the trained ML model.

- Model predicts the best-suited crop.

- Result is displayed on the web interface.

## 🖼️ Screenshots

<img width="927" height="566" alt="Home Page" src="https://github.com/user-attachments/assets/33bfd95d-84ad-46ec-bc09-6ba4d78d46b3" />
<img width="1918" height="861" alt="Predict Page" src="https://github.com/user-attachments/assets/9edac9af-da9d-4b67-8101-ea05643181a2" />
<img width="1915" height="865" alt="Result Page" src="https://github.com/user-attachments/assets/2d6b1839-cd59-462f-b7db-5d9fb198bb66" />

## 🤝 Contributing

Pull requests are welcome!

For major changes, please open an issue first to discuss what you’d like to change.


## 👩‍💻 Author
  Harati Gadre
  
🌐 GitHub: https://github.com/haratiGadre

📧 gadre.harati814@gmail.com
