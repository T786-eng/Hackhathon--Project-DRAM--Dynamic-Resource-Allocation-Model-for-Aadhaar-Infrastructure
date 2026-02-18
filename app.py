import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="Project DRAM | UIDAI Dashboard", 
    layout="wide", 
    page_icon="🆔"
)

# Custom Professional Styling
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e6e9ef; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    [data-testid="stMetricValue"] { font-size: 28px; color: #1f77b4; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("final_district_classification.csv")
        summary = pd.read_csv("executive_summary.csv")
        df['Youth_Ratio'] = df['Youth_Ratio'].fillna(0)
        return df, summary
    except Exception as e:
        st.error("⚠️ Error: Processed data not found. Run 'python main.py' first.")
        st.stop()

df, summary = load_data()

# --- 3. SIDEBAR: THE CONTROL PANEL ---
st.sidebar.image("https://uidai.gov.in/images/logo/aadhaar_english_logo.svg", width=180)
st.sidebar.title("🛠️ Deployment Controls")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Project Source")
st.sidebar.markdown("[📂 **View Project Github**](https://github.com/T786-eng/Hackhathon--Project-DRAM--Dynamic-Resource-Allocation-Model-for-Aadhaar-Infrastructure.git)")
st.sidebar.markdown("---")

st.sidebar.subheader("📍 Region Filter")
all_states = sorted(df['state'].unique())
selected_states = st.sidebar.multiselect("Select States", options=all_states)

st.sidebar.subheader("⚖️ Priority Filter")
all_zones = sorted(df['Zone_Strategy'].unique())
selected_zones = st.sidebar.multiselect("Select Zone Types", options=all_zones)

st.sidebar.subheader("🔍 Local Search")
search_query = st.sidebar.text_input("Search District or Place Name")

filtered_df = df.copy()
if selected_states:
    filtered_df = filtered_df[filtered_df['state'].isin(selected_states)]
if selected_zones:
    filtered_df = filtered_df[filtered_df['Zone_Strategy'].isin(selected_zones)]
if search_query:
    filtered_df = filtered_df[filtered_df['district'].str.contains(search_query, case=False, na=False)]

st.sidebar.divider()
csv_download = filtered_df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="📥 Download Deployment List (CSV)",
    data=csv_download,
    file_name='aadhaar_deployment_plan.csv',
    mime='text/csv'
)

# --- 4. MAIN DASHBOARD ---
st.title("📊 Project DRAM v2.0")

# --- ADDED: PROJECT DESCRIPTION SUMMARY ---
with st.expander("📖 Project Summary & Problem Statement", expanded=True):
    st.write("""
    **Objective:** To unlock societal trends in Aadhaar usage and optimize infrastructure deployment. 
    
    **The Problem:** uniform resource allocation is inefficient. Some districts are "Update-Heavy" while others still need "New Enrolments."
    
    **The Solution:** We use the **UER (Update-to-Enrolment Ratio)** to classify districts into 3 Strategic Zones. This ensures that RED zones get permanent Update Hubs, while GREEN zones receive mobile Enrolment Vans, saving costs and improving citizen service.
    """)

# KPI Row
c1, c2, c3, c4 = st.columns(4)
c1.metric("Districts in View", len(filtered_df))
c2.metric("Red Zone Districts", len(filtered_df[filtered_df['Zone_Strategy'].str.contains('RED')]))
c3.metric("Avg. National UER", f"{summary['Average_UER'].iloc[0]}")
c4.metric("Transitions Expected", int(summary['Districts_Expected_to_Transition'].iloc[0]))

# Visualizations Row
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🌐 Resource Hierarchy")
    fig_sun = px.sunburst(
        filtered_df, path=['state', 'Zone_Strategy'], values='Updates',
        color='Zone_Strategy',
        color_discrete_map={'RED: Express Update Hub': '#d62728', 'YELLOW: Hybrid Center': '#ff7f0e', 'GREEN: Enrolment Van': '#2ca02c'}
    )
    st.plotly_chart(fig_sun, width='stretch')
    # --- ADDED: PLOT DESCRIPTION ---
    st.caption("**What is this?** This Sunburst chart shows the distribution of service needs by State. The larger the slice, the higher the volume of updates required in that region.")

with col_right:
    st.subheader("📈 Demand Pattern Analysis")
    fig_scatter = px.scatter(
        filtered_df, x="Enrolments", y="Updates", color="Zone_Strategy", 
        hover_name="district", size="UER", log_x=True, log_y=True,
        color_discrete_map={'RED: Express Update Hub': '#d62728', 'YELLOW: Hybrid Center': '#ff7f0e', 'GREEN: Enrolment Van': '#2ca02c'}
    )
    st.plotly_chart(fig_scatter, width='stretch')
    # --- ADDED: PLOT DESCRIPTION ---
    st.caption("**What is this?** This scatter plot identifies 'Saturation.' Districts in the top-left (RED) are fully enrolled and only need maintenance, while those in the bottom-right (GREEN) still require primary enrolment infrastructure.")

# Deployment Table
st.divider()
st.subheader("📋 Targeted Deployment Table")
table_display = filtered_df[['state', 'district', 'UER', 'Zone_Strategy', 'Predicted_Trajectory']].sort_values('UER', ascending=False)
st.dataframe(table_display, width='stretch', hide_index=True)

# PNG Reports Section
with st.expander("🖼️ View Deep-Dive Visual Reports"):
    tabs = st.tabs(["Pattern Proof", "Anomaly Detection", "Demographics"])
    with tabs[0]:
        if os.path.exists('3_enrolments_vs_updates.png'): st.image('3_enrolments_vs_updates.png')
    with tabs[1]:
        if os.path.exists('4_anomaly_detection.png'): st.image('4_anomaly_detection.png')
    with tabs[2]:
        if os.path.exists('5_demographic_insights.png'): st.image('5_demographic_insights.png')