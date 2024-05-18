import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    return joblib.load('energy_model.pkl')
# model = joblib.load('energy_model.pkl')
model = load_model()

# Streamlit app
def main():
    st.title("Average Hourly Energy Consumption Prediction")

    #taking inputs from the user
    day = st.selectbox('Day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    season = st.selectbox('Season', ['Summer', 'Winter', 'Autumn', 'Monsoon'])
    avg_temp = st.slider('Average Temperature (°C)', min_value=5, max_value=50)
    avg_hum = st.slider('Average Humidity (%)', min_value=1, max_value=100)

    if st.button('Predict'):
        #loading the pretrained ml model
        model = joblib.load('energy_model.pkl')

        input_data = pd.DataFrame({
            'Avg_Temp': [avg_temp],
            'Avg_Hum': [avg_hum],
            'Day': [day],
            'Season': [season]
        })

        # Predict
        prediction = model.predict(input_data)
        st.markdown(f"""
        <div 
            <h2 style="font-size: 18px; text-align: center;">Predicted Average Energy Consumption per hour</h2>
            <p style="font-size: 32px; text-align: center;">
                <span>{prediction[0]:.2f}</span>
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
