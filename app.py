import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --- Page Configuration MUST BE THE FIRST STREAMLIT COMMAND ---
st.set_page_config(
    page_title="The Machine Doctor",
    page_icon="🤖",
    layout="wide"
)

# --- 1. Load the trained model and features ---
@st.cache_resource
def load_model_assets():
    """Loads the saved model and features."""
    try:
        model = joblib.load('rul_model.joblib')
        features = joblib.load('features.joblib')
        return model, features
    except FileNotFoundError:
        return None, None

model, features = load_model_assets()

# --- 2. Title and Description ---
st.title("🤖 The Machine Doctor: Predictive Maintenance AI")
st.markdown(
    "**Project Overview:** This application demonstrates a predictive maintenance model trained on the NASA Turbofan Engine "
    "Degradation dataset. It uses a Random Forest Regressor to predict the Remaining Useful Life (RUL) of an engine "
    "based on its **normalized sensor values (0-1)**. Adjust the sliders in the sidebar and click 'Predict' to see an instant health assessment."
)
st.divider()

# --- 3. Input Sidebar ---
st.sidebar.header("Machine Input Parameters")
st.sidebar.markdown("Adjust the normalized sensor values below.")

input_data = {}
if features:
    for feature in features:
        input_data[feature] = st.sidebar.slider(
            label=feature, min_value=0.0, max_value=1.0, value=0.5, step=0.01
        )
else:
    st.sidebar.error("Feature list not found. Please ensure 'features.joblib' is in the folder.")

# --- 4. Prediction and Display Logic ---
if st.button("Predict Health Status", type="primary", use_container_width=True):
    if model is not None and features is not None:
        input_df = pd.DataFrame([input_data], columns=features)
        prediction = model.predict(input_df)
        predicted_rul = int(round(prediction[0]))

        if predicted_rul > 100:
            health_status = "🟢 Healthy"
            recommendation = "No immediate action required. Continue routine monitoring."
        elif 50 <= predicted_rul <= 100:
            health_status = "🟡 Warning"
            recommendation = "Engine shows moderate wear. Schedule maintenance soon."
        else:
            health_status = "🔴 Critical"
            recommendation = "Failure is likely imminent. Immediate maintenance required."

        # Display results in simple, clean columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Predicted RUL", value=f"{predicted_rul} cycles")
        with col2:
            st.metric(label="Machine Health Status", value=health_status)
        with col3:
            # Use standard Streamlit components for simplicity and robustness
            st.subheader("Recommendation")
            st.write(recommendation)

    else:
        st.error("Model or feature files not found. Please ensure the model has been trained and the .joblib files are in the correct folder.")

