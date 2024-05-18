import streamlit as st
import pandas as pd
import numpy as np
import joblib



model = joblib.load('energy_model.pkl')

# Streamlit app
def main():
    st.title("Energy Consumption Prediction")

    # Input fields for the user to provide data
    day = st.selectbox('Day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    season = st.selectbox('Season', ['Summer', 'Winter', 'Autumn', 'Monsoon'])
    # max_tem = st.number_input('Max Temperature')
    # min_tem = st.number_input('Min Temperature')
    # max_hum = st.number_input('Max Humidity')
    # min_hum = st.number_input('Min Humidity')
    avg_temp = st.slider('Average Temperature (°C)', min_value=5, max_value=50)
    avg_hum = st.slider('Average Humidity (%)', min_value=1, max_value=100)
    # min_load = st.number_input('Min Load')
    # max_load = st.number_input('Max Load')

    if st.button('Predict'):
        # Load the model
        model = joblib.load('energy_model.pkl')

        # Create a DataFrame from user inputs
        input_data = pd.DataFrame({
            # 'Max_Tem': [max_tem],
            # 'Min_Tem': [min_tem],
            # 'Max_Hum': [max_hum],
            # 'Min_Hum': [min_hum],
            'Avg_Temp': [avg_temp],
            'Avg_Hum': [avg_hum],
            # 'Min_Load': [min_load],
            # 'Max_Load': [max_load],
            'Day': [day],
            'Season': [season]
        })

        # Predict
        prediction = model.predict(input_data)

        st.write(f"Predicted Average Energy Consumption per hour: {prediction[0]:.2f}")

if __name__ == '__main__':
    main()
