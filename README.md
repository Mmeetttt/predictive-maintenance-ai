# 🤖 The Machine Doctor: Predictive Maintenance AI

**The Machine Doctor** is a machine learning–powered web application that predicts the **Remaining Useful Life (RUL)** of industrial machinery — specifically turbofan engines — using simulated sensor data from the **NASA Prognostics Data Repository**.  

The system helps anticipate equipment failures before they occur, enabling proactive maintenance and reducing costly downtime.

---

## 🚀 Overview

This project demonstrates how **data analytics and predictive modeling** can transform industrial maintenance into a **data-driven process**.  
It combines a **Random Forest Regressor** for RUL prediction with a **Streamlit dashboard** for interactive visualization and user input.

---

## ✨ Key Features

- 🧩 **Interactive Dashboard:** Users can manipulate normalized sensor readings via sliders to simulate different operating conditions.  
- ⚡ **Real-Time Prediction:** Instantly calculates the predicted Remaining Useful Life (RUL) of the machine.  
- 🧠 **Smart Recommendations:** Provides clear, actionable maintenance suggestions based on model predictions.  
- 📊 **Data-Driven Insights:** Visualizes trends and degradation patterns to enhance understanding of equipment health.  

---

## 🧰 Tech Stack

| Category | Tools & Libraries |
|-----------|------------------|
| **Language** | Python |
| **Framework** | Streamlit |
| **Machine Learning** | scikit-learn (Random Forest Regressor) |
| **Data Handling** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Dataset** | NASA Turbofan Engine Degradation Simulation Data Set |

---

## 🛠️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mmeetttt/predictive-maintenance-ai.git
   cd predictive-maintenance-ai
2. Install dependencies:
    Pip install -r requirements.txt


4. Run the Streamlit app:
    streamlit run app.py


Open in browser:
Visit http://localhost:8501 to explore the dashboard.
