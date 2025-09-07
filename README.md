🤖 The Machine Doctor: Predictive Maintenance AI

This project is a web application that demonstrates a predictive maintenance model for industrial machinery. It predicts the Remaining Useful Life (RUL) of a turbofan engine based on simulated sensor data from the NASA Prognostics Data Repository.

The application is built in Python using Streamlit for the front-end and a Random Forest Regressor from scikit-learn for the machine learning model.

✨ Features
Interactive Dashboard: Users can adjust normalized sensor values using sliders.

Real-Time Prediction: Get an instant health assessment and RUL prediction.

Clear Recommendations: Provides actionable maintenance advice based on the prediction.

🚀 Live Demo(After you deploy to Hugging Face, you can add the link here!)
📸 Screenshot(You can add a screenshot of your running application here)

🛠️ How to Run Locally
Clone the repository:

git clone [https://github.com/YourUsername/YourProjectRepo.git](https://github.com/YourUsername/YourProjectRepo.git)
cd YourProjectRepo

Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

📚 Dataset
This model was trained on the Turbofan Engine Degradation Simulation Data Set provided by NASA.