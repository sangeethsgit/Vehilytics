import streamlit as st

st.set_page_config(page_title="Vehicle Health Monitoring", layout="wide")

# Create columns to simulate side margins
left_col, main_col, right_col = st.columns([1, 6, 1])  # Adjust ratios as needed

with main_col:
    st.title("Vehicle Health Monitoring System")
    st.markdown("### Powered by Simulated Data for Explorative Data Analysis")

    st.markdown("""
                
    ### Project Overview
    This application simulates and analyzes vehicle performance using **categorical predictors** to forecast important health indicators such as mileage, engine health, and service needs.

    It provides an **interactive dashboard** to support preventive maintenance, diagnostics, and fuel efficiency monitoring.

    ### Key Objectives

    - Predict whether a vehicle's **mileage** is high or low
    - Estimate **continuous mileage** (in km/l) based on input features
    - Assess **engine health** (good/bad)
    - Detect whether **service is required** (yes/no)
    - Enable **interactive filtering** and visualization using Streamlit

    ### Input Features

    | Feature           | Values                          |
    |------------------|----------------------------------|
    | Oil Level        | empty, full                  |
    | Terrain          | plain, desert, mountain    |
    | Tyre Condition   | good, bad                    |
    | Battery Voltage  | high, low                    |
    | Vehicle Type     | 2-wheeler, 4-wheeler, 6-wheeler |

    ### Output Targets

    | Target Variable      | Type          | Values / Description             |
    |----------------------|---------------|----------------------------------|
    | Mileage (km/l)       | Continuous    | Estimated fuel efficiency        |
    | Mileage Category     | Categorical   | high / low                   |
    | Engine Health        | Categorical   | good / bad                   |
    | Service Required     | Categorical   | yes / no                     |

    ### Applications

    - Real-time vehicle health dashboards
    - Fleet management tools for service centers
    - Data-driven predictive maintenance systems
    - Automotive ML model training and validation

    ### Technologies Used

    - **Python** for simulation and processing  
    - **Streamlit** for interactive dashboard  
    - **Pandas & NumPy** for data manipulation  
    - **Matplotlib & Seaborn** for visualization  
    """)
