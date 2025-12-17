House Price Prediction Web App:

A Machine Learning web application that predicts house prices based on user-provided inputs such as living area, number of bedrooms, and bathrooms.
The application is built using Python, Linear Regression, and Streamlit, and is deployed on Streamlit Community Cloud.
Live Demo

👉 [https://sctml01-w9jmwfweqvu9cbon8x6t28.streamlit.app/]
Project Overview:

House prices depend on several factors such as property size and room count.
This project uses a Linear Regression model trained on real housing data to estimate house prices based on:

Living Area (square feet)

Number of Bedrooms

Number of Bathrooms

The trained model is integrated into an interactive Streamlit web application that allows users to enter values and instantly view the predicted price.
Machine Learning Details

Algorithm Used: Linear Regression

Type: Supervised Learning (Regression)

Target Variable: SalePrice

Input Features:

GrLivArea – Above ground living area (sq ft)

BedroomAbvGr – Number of bedrooms

FullBath – Number of full bathrooms

The model is trained using the scikit-learn library.
🛠️ Technologies Used

Python

Streamlit (Web App Framework)

Pandas (Data Handling)

Scikit-learn (Machine Learning)

GitHub (Version Control & Deployment)

Streamlit Community Cloud (Hosting)

🖥️ Application Features

Interactive user input via sliders and dropdowns

Real-time house price prediction

Clean and professional UI

Uses a real machine learning model (not hardcoded values)

Deployed and accessible via a public URL

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
