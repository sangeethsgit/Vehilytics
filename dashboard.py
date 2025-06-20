# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_csv(r"D:\CDAC Internship\DOCS\simulated_mileage_dataset.csv")

# # Sidebar filters
# st.sidebar.title("Filter Predictors")
# oil_level = st.sidebar.selectbox("Oil Level", ["All"] + sorted(df['Oil Level'].unique()))
# terrain = st.sidebar.selectbox("Terrain", ["All"] + sorted(df['Terrain'].unique()))
# tyre_condition = st.sidebar.selectbox("Tyre Condition", ["All"] + sorted(df['Tyre Condition'].unique()))
# battery_voltage = st.sidebar.selectbox("Battery Voltage", ["All"] + sorted(df['Battery Voltage'].unique()))
# vehicle_type = st.sidebar.selectbox("Vehicle Type", ["All"] + sorted(df['Vehicle Type'].unique()))

# # Apply filters
# filtered_df = df.copy()
# if oil_level != "All":
#     filtered_df = filtered_df[filtered_df["Oil Level"] == oil_level]
# if terrain != "All":
#     filtered_df = filtered_df[filtered_df["Terrain"] == terrain]
# if tyre_condition != "All":
#     filtered_df = filtered_df[filtered_df["Tyre Condition"] == tyre_condition]
# if battery_voltage != "All":
#     filtered_df = filtered_df[filtered_df["Battery Voltage"] == battery_voltage]
# if vehicle_type != "All":
#     filtered_df = filtered_df[filtered_df["Vehicle Type"] == vehicle_type]

# st.title("Vehicle Health Dashboard")
# st.markdown("Use the sidebar to filter predictors and explore target variable distributions.")

# # 1. Mileage (continuous) Histogram
# st.subheader("Mileage Distribution (km/l)")
# fig1, ax1 = plt.subplots()
# sns.histplot(filtered_df['Mileage (km/l)'], bins=15, kde=True, ax=ax1, color='skyblue')
# st.pyplot(fig1)

# # 2. Mileage Category (Bar Chart)
# st.subheader("Mileage Category Distribution")
# fig2, ax2 = plt.subplots()
# mileage_cat_counts = filtered_df['Mileage Category'].value_counts()
# ax2.bar(mileage_cat_counts.index, mileage_cat_counts.values, color=sns.color_palette('pastel'))
# ax2.set_ylabel("Count")
# ax2.set_xlabel("Mileage Category")
# ax2.set_title("Mileage Category (High/Low)")
# st.pyplot(fig2)

# # 3. Engine Health (Donut Chart)
# st.subheader("Engine Health Distribution")
# fig3, ax3 = plt.subplots()
# engine_counts = filtered_df['Engine Health'].value_counts()
# ax3.pie(engine_counts, labels=engine_counts.index, autopct='%1.1f%%',
#         colors=sns.color_palette('Set2'), startangle=90,
#         wedgeprops={'width': 0.4})
# ax3.axis('equal')
# st.pyplot(fig3)

# # 4. Service Required (Pie Chart)
# st.subheader("Service Requirement Distribution")
# fig4, ax4 = plt.subplots()
# service_counts = filtered_df['Service Required'].value_counts()
# ax4.pie(service_counts, labels=service_counts.index, autopct='%1.1f%%',
#         colors=sns.color_palette('pastel'))
# ax4.axis('equal')
# st.pyplot(fig4)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Vehicle Health Dashboard", layout="wide")
# df = pd.read_csv(r"D:\CDAC Internship\DOCS\simulated_mileage_dataset.csv")


# st.sidebar.title("Filter Predictors")
# oil_level = st.sidebar.selectbox("Oil Level",sorted(df['Oil Level'].unique()))
# terrain = st.sidebar.selectbox("Terrain",sorted(df['Terrain'].unique()))
# tyre_condition = st.sidebar.selectbox("Tyre Condition",sorted(df['Tyre Condition'].unique()))
# battery_voltage = st.sidebar.selectbox("Battery Voltage",sorted(df['Battery Voltage'].unique()))
# vehicle_type = st.sidebar.selectbox("Vehicle Type",sorted(df['Vehicle Type'].unique()))

# filtered_df = df.copy()
# filtered_df = filtered_df[filtered_df["Oil Level"] == oil_level]
# filtered_df = filtered_df[filtered_df["Terrain"] == terrain]
# filtered_df = filtered_df[filtered_df["Tyre Condition"] == tyre_condition]
# filtered_df = filtered_df[filtered_df["Battery Voltage"] == battery_voltage]
# filtered_df = filtered_df[filtered_df["Vehicle Type"] == vehicle_type]


# st.markdown("<h1 style='text-align: center; color: #ffff00;'>Vehicle Health Dashboard</h1>", unsafe_allow_html=True)
# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("Mileage Distribution (km/l)")
#     fig1, ax1 = plt.subplots(figsize=(8,4))
#     sns.histplot(filtered_df['Mileage (km/l)'], bins=15, kde=True, ax=ax1, color='#ff0048')
#     ax1.set_xlabel("Mileage (km/l)")
#     ax1.set_ylabel("Number of Vehicles")
#     st.pyplot(fig1)

# with col2:
#     st.subheader("Mileage Category Distribution")
#     fig2, ax2 = plt.subplots(figsize=(8,4))
#     mileage_cat_counts = filtered_df['Mileage Category'].value_counts()
#     ax2.bar(mileage_cat_counts.index, mileage_cat_counts.values, color=sns.color_palette('deep'))
#     ax2.set_ylabel("Number of Vehicles")
#     ax2.set_xlabel("Mileage Category")
#     st.pyplot(fig2)

# col3, col4 = st.columns(2)

# with col3:
#     st.subheader("Engine Health")
#     fig3, ax3 = plt.subplots(figsize=(8,4))
#     engine_counts = filtered_df['Engine Health'].value_counts()
#     ax3.pie(engine_counts, labels=engine_counts.index, autopct='%1.1f%%',
#             colors=sns.color_palette('dark'), startangle=90,
#             wedgeprops={'width': 0.4})
#     ax3.axis('equal')
#     st.pyplot(fig3)

# with col4:
#     st.subheader("Service Required")
#     fig4, ax4 = plt.subplots(figsize=(8,4))
#     service_counts = filtered_df['Service Required'].value_counts()
#     ax4.pie(service_counts, labels=service_counts.index, autopct='%1.1f%%',
#             colors=sns.color_palette('colorblind'))
#     ax4.axis('equal')
#     st.pyplot(fig4)



# if not filtered_df.empty:
#     predicted_mileage = round(filtered_df["Mileage (km/l)"].mean(), 2)

#     st.html(f"""
# <div style='
#     width: 320px;
#     background: linear-gradient(135deg, #003049, #264653);
#     padding: 25px;
#     border-radius: 15px;
#     box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
#     text-align: center;
#     margin: 30px auto;
#     font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
# '>
#     <h3 style='
#         color: #ffff00;
#         margin-bottom: 12px;
#         font-size: 22px;
#         font-weight: 600;
#         letter-spacing: 0.8px;
#     '>Estimated Mileage</h3>

#     <p style='
#         font-size: 32px;
#         font-weight: bold;
#         color: #f1faee;
#         margin: 0;
#     '>{predicted_mileage} <span style='font-size:18px;'>km/l</span></p>
# </div>
# """,)



# else:
#     st.markdown(f"""
#     <div style='
#         background-color: #fff3cd;
#         padding: 20px;
#         border-radius: 10px;
#         border: 1px solid #ffeeba;
#         text-align: center;
#         margin-top: 20px;'>
#         <h4 style='color: #856404;'>No data available for the selected combination of predictors.</h4>
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Vehicle Health Dashboard", layout="wide")

df = pd.read_csv(r"D:\CDAC Internship\DOCS\simulated_mileage_dataset.csv")


st.sidebar.title("Filter Predictors")
oil_level = st.sidebar.selectbox("Oil Level", df['Oil Level'].unique())
terrain = st.sidebar.selectbox("Terrain", sorted(df['Terrain'].unique()))
tyre_condition = st.sidebar.selectbox("Tyre Condition", df['Tyre Condition'].unique())
battery_voltage = st.sidebar.selectbox("Battery Voltage", (df['Battery Voltage'].unique()))
vehicle_type = st.sidebar.selectbox("Vehicle Type", df['Vehicle Type'].unique())


filtered_df = df.copy()
filtered_df = filtered_df[filtered_df["Oil Level"] == oil_level]
filtered_df = filtered_df[filtered_df["Terrain"] == terrain]
filtered_df = filtered_df[filtered_df["Tyre Condition"] == tyre_condition]
filtered_df = filtered_df[filtered_df["Battery Voltage"] == battery_voltage]
filtered_df = filtered_df[filtered_df["Vehicle Type"] == vehicle_type]


st.markdown("<h1 style='text-align: center; color: #ffff00;'>Vehicle Health Dashboard</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Mileage Distribution (km/l)")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.histplot(filtered_df['Mileage (km/l)'], bins=15, kde=True, ax=ax1, color='#ff0048')
    ax1.set_xlabel("Mileage (km/l)")
    ax1.set_ylabel("Number of Vehicles")
    st.pyplot(fig1)

with col2:
    st.subheader("Mileage Category Distribution")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    mileage_cat_counts = filtered_df['Mileage Category'].value_counts()
    ax2.bar(mileage_cat_counts.index, mileage_cat_counts.values, color=sns.color_palette('deep'))
    ax2.set_ylabel("Number of Vehicles")
    ax2.set_xlabel("Mileage Category")
    st.pyplot(fig2)

col3, col4 = st.columns(2)
with col3:
    st.subheader("Engine Health")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    engine_counts = filtered_df['Engine Health'].value_counts()
    ax3.pie(engine_counts, labels=engine_counts.index, autopct='%1.1f%%',
            colors=sns.color_palette('dark'), startangle=90,
            wedgeprops={'width': 0.4})
    ax3.axis('equal')
    st.pyplot(fig3)

with col4:
    st.subheader("Service Required")
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    service_counts = filtered_df['Service Required'].value_counts()
    ax4.pie(service_counts, labels=service_counts.index, autopct='%1.1f%%',
            colors=sns.color_palette('colorblind'))
    ax4.axis('equal')
    st.pyplot(fig4)



predicted_mileage = round(filtered_df["Mileage (km/l)"].mean(), 2)
below_30_pct = round((filtered_df["Mileage (km/l)"] < 30).mean() * 100, 2)

col_kpi1, col_kpi2 = st.columns(2)


with col_kpi1:
    st.html(f"""
    <div style='
        width: 100%;
        background: #ffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        text-align: center;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    '>
        <h3 style='
            color: #000000;
            margin-bottom: 12px;
            font-size: 22px;
            font-weight: 600;
            letter-spacing: 0.8px;
        '>Estimated Mileage</h3>

        <p style='
            font-size: 32px;
            font-weight: bold;
            color: #b30427;
            margin: 0;
        '>{predicted_mileage} <span style='font-size:18px;'>km/l</span></p>
    </div>
    """,)

with col_kpi2:
    st.html(f"""
    <div style='
        width: 100%;
        background: #ffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        text-align: center;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    '>
        <h3 style='
            color: #000000;
            margin-bottom: 12px;
            font-size: 22px;
            font-weight: 600;
            letter-spacing: 0.8px;
        '>Vehicles Below 30 km/l</h3>

        <p style='
            font-size: 32px;
            font-weight: bold;
            color: #b30427;
            margin: 0;
        '>{below_30_pct}%</p>
    </div>
    """, )

max_mileage = round(df["Mileage (km/l)"].max(), 2)
st.html(f"""
<div style='
    width: 50%;
    background: #ffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    text-align: center;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    margin-left: 305px;
'>
    <h3 style='
        color: #000000;
        margin-bottom: 12px;
        font-size: 22px;
        font-weight: 600;
        letter-spacing: 0.8px;
    '>Maximum Estimated Mileage</h3>

    <p style='
        font-size: 32px;
        font-weight: bold;
        color: #b30427;
        margin: 0;
    '>{max_mileage} <span style='font-size:18px;'>km/l</span></p>
</div>
""")