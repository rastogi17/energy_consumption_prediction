# Electricity Demand Prediction Model Deployment for SEWA
SEWA - Sharjah Electricity and Water Authority

This repository contains code for deploying an electricity demand prediction model using XGBoost, which demonstrated the best performance among several tried and tested models. The model is deployed using Streamlit and hosted on Render.

## Business Logic Understanding

The dataset used for this project contains historical data from 2021 on various factors influencing electricity demand, such as temperature, humidity, day, and date. By analyzing this data, insights into underlying patterns and trends in electricity consumption can be gained.

Variables considered for predicting electricity demand include temperature and humidity metrics, as these factors influence energy consumption patterns. Additionally, features like day and season were extracted from the date and day columns to capture temporal variations in demand. Only average values of temperature and humidity were used to better predict energy demand, as the minimum and maximum values showed high correlation, which could introduce overfitting due to multicollinearity.

## Technical Approach

### Data Cleaning
- Data type correction was performed by cleaning the data and removing unnecessary strings.
- Missing values were dropped from the dataset, as less than 5% of the data contained null values.

### Exploratory Data Analysis (EDA)
- Pandas "describe" function and box plots were utilized to identify outliers, which were removed from columns like 'Max_Hum' and 'Avg_Hum'.
- Correlation matrix was used to identify correlations between variables and address multicollinearity concerns.
- Features like seasonality were extracted from the date column.
- One Hot Encoding was performed to convert categorical columns (day and season) into numerical format.

### Data Preprocessing
- Selected average temperature and humidity columns to mitigate multicollinearity and potential overfitting.
- Defined input features (average temperature, average humidity, days, and seasons) and output feature (average energy load per hour).
- Standard Scaler was used to standardize the data.

### Model Training and Evaluation
- Various regression models were fitted to the training data, including Linear Regression, Ridge Regression, Support Vector Regression (SVR), Random Forest Regression, and XGBoost Regression.
- Hyperparameters were tuned using techniques like GridSearchCV to optimize model performance.
- Model performance was evaluated using metrics such as Root Mean Squared Error (RMSE) and R^2 score to assess predictive accuracy.

## Deployment
The XGBoost regression model, which demonstrated the best performance, was deployed using Streamlit and hosted on Render for easy access and interaction.

## Repository Structure

- **app.py**: Contains the Streamlit application code.
- **requirements.txt**: Lists the required dependencies for running the application.
- **energy_model.pkl**: Best performing model - XGBoost model for deployment.
- **SEWA_energy.csv**: Dataset containing the historical data used for training and testing.
- **model_train.ipynb**: Jupyter Notebook file containing data cleaning, preprocessing, and model training steps.

## Usage

To run the application locally, make sure you have Python and the required dependencies installed. Then, execute the following commands:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Access the deployed application on Render at [link-to-render-app](https://energyprediction.onrender.com).

---
