<div align="center">
  <h1><b>FastAPI-Sepsis-Prediction-API</b></h1>
</div>

# 📕 Table of Contents

- [📕 Table of Contents](#table-of-contents)
- [🎈 Introduction](#introduction)
- [🛠 Project Structure](#project-structure)
- [📝 Overview](#overview)
- [🔧 Installation](#installation)
- [🚀 Usage](#usage)
- [🤝 Contributing](#contributing)
- [🔏 License](#license)
- [📚 References](#references)
- [👤 Author](#author)

## 🎈 Introduction
In the fast-paced world of healthcare, every second counts. Timely intervention can mean the difference between life and death, especially when it comes to critical conditions like sepsis. Our FastAPI Sepsis Prediction project aims to harness the power of AI to transform patient care and save lives by predicting sepsis onset in real-time.

## ♻ Data Features
- **ID**: Unique patient identification number.
- **PRG**: Plasma glucose level (mmol/L).
- **PL**: Blood work result 1 (mu U/ml).
- **PR**: Blood pressure (mm Hg).
- **SK**: Blood work result 2 (mm).
- **TS**: Blood work result 3 (mu U/ml).
- **M11**: Body mass index (weight in kg/(height in m)²).
- **BD2**: Blood work result 4 (mu U/ml).
- **Age**: Patient’s age (years).
- **Insurance**: Indication of whether the patient holds a valid insurance card.
- **Sepsis**: Classification indicating whether the patient has sepsis (Positive) or not (Negative).

## 🛠 Project Structure
FastAPI-Sepsis-Prediction
├── data
│ └── patient_data.csv # Dataset containing patient information
├── models
│ └── sepsis_prediction_model.joblib # Trained machine learning model
├── notebooks
│ └── data_exploration.ipynb # Jupyter notebook for data exploration
├── src
│ ├── app.py # FastAPI application for sepsis prediction
│ └── utils.py # Utility functions for data preprocessing
├── README.md # Project overview and instructions
└── requirements.txt # Dependencies required for running the project


## 📝 Overview
This project utilizes machine learning algorithms and FastAPI to predict sepsis onset in real-time. By analyzing patient data, our API provides clinicians with early warnings of potential sepsis occurrences, enabling proactive intervention and improved patient outcomes.

## 🔧 Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.

## 🚀 Usage
1. Navigate to `main.py`
2. Run the FastAPI application: `uvicorn app:app --host 0.0.0.0 --port 8000`.
3. Access the API endpoints to predict sepsis onset and integrate the API into existing healthcare systems.

## 📝 Article
Read the article on this project [Here](https://www.linkedin.com/pulse/revolutionizing-healthcare-ai-predicting-sepsis-efosa-dave-omosigho-kmhvf)

## 🤝 Contributing
If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Make your changes.
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.

## 🔏 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📚 References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)

## 👤 AUTHOR
🤵 **Efosa Dave Omosigho**
- [GitHub Profile](https://github.com/Elphoxa) 🐙
- [LinkedIn Profile](https://www.linkedin.com/in/efosa-omosigho) 💼
