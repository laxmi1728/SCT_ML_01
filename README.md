House Price Prediction Web App:

A Machine Learning web application that predicts house prices based on user-provided inputs such as living area, number of bedrooms, and bathrooms.
The application is built using Python, Linear Regression, and Streamlit, and is deployed on Streamlit Community Cloud.
Live Demo

👉 [https://sctml01-w9jmwfweqvu9cbon8x6t28.streamlit.app/]

## 📌 Project Overview

House price prediction is an important real-world problem in real estate.  
This application uses a **Linear Regression model** trained on housing data to estimate the selling price of a house based on:

- Living Area (square feet)
- Number of Bedrooms
- Number of Bathrooms

Users can enter these values through a web interface and instantly get a predicted price.

---

## 🧠 Machine Learning Details

- **Algorithm Used:** Linear Regression  
- **Learning Type:** Supervised Learning (Regression)  
- **Target Variable:** `SalePrice`  

### Input Features:
- `GrLivArea` – Above ground living area (sq ft)
- `BedroomAbvGr` – Number of bedrooms
- `FullBath` – Number of full bathrooms

The model is implemented using **scikit-learn**.

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- GitHub  
- Streamlit Community Cloud  

---

## ✨ Application Features

- Interactive user inputs (sliders & dropdowns)
- Real-time house price prediction
- Clean and professional UI
- Uses a real machine learning model
- Deployed as a live web application

📁 Project Structure
house-price-streamlit/
│── app.py                # Streamlit application code
│── train.csv             # Dataset used for training
│── requirements.txt      # Required Python libraries
│── README.md             # Project documentation

▶️ How to Run the Project Locally

Clone the repository:

git clone https://github.com/laxmi1728/SCT_ML_01.git


Navigate to the project folder:

cd SCT_ML_01


Install required libraries:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

🌐 Deployment

The application is deployed using Streamlit Community Cloud by connecting the GitHub repository SCT_ML_01 and selecting app.py as the main file.

🎯 Future Enhancements

Add more house features (location, year built, etc.)

Improve accuracy using advanced regression models

Save and load the trained model

Add data visualizations

👩‍💻 Author

Thota Laxmi Prasanna
Machine Learning Intern

📜 License

This project is created for learning and educational purposes.
