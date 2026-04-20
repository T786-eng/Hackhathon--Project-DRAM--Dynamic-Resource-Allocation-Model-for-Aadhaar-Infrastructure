import streamlit as st
import pandas as pd
import plotly.express as px
import os
from typing import Tuple, Optional

# --- 1. GLOBAL CONFIGURATION & UI THEME ---
ZONE_COLORS = {
    'RED: Express Update Hub': '#B02E0C',
    'YELLOW: Hybrid Center': '#EBA10E',
    'GREEN: Enrolment Van': '#057A55'
}
REQUIRED_FILES = ["final_district_classification.csv", "executive_summary.csv"]

st.set_page_config(
    page_title="Project DRAM | Infrastructure Intelligence", 
    layout="wide", 
    page_icon="🆔"
)

# Professional CSS for Component Isolation
st.markdown("""
    <style>
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #1f77b4; }
    [data-testid="stMetricValue"] { font-size: 1.8rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA ENGINE ---
@st.cache_data(ttl=3600)
def load_and_validate_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    if not all(os.path.exists(f) for f in REQUIRED_FILES):
        st.error("FATAL: System dependencies missing. Execute 'main.py' first.")
        st.stop()
    try:
        df = pd.read_csv(REQUIRED_FILES[0])
        summary = pd.read_csv(REQUIRED_FILES[1])
        df['Youth_Ratio'] = df['Youth_Ratio'].fillna(0)
        return df, summary
    except Exception as e:
        st.error(f"CRITICAL: Data integrity fault: {e}")
        st.stop()

df, summary = load_and_validate_data()

# --- 3. SIDEBAR CONTROLS ---
def render_sidebar(data: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.image("https://uidai.gov.in/images/logo/aadhaar_english_logo.svg", width=180)
    st.sidebar.title("System Controls")
    st.sidebar.markdown("---")
    
    states = st.sidebar.multiselect("Region Scope", sorted(data['state'].unique()))
    zones = st.sidebar.multiselect("Strategy Filter", sorted(data['Zone_Strategy'].unique()))
    search = st.sidebar.text_input("District Lookup")
    
    mask = pd.Series(True, index=data.index)
    if states: mask &= data['state'].isin(states)
    if zones: mask &= data['Zone_Strategy'].isin(zones)
    if search: mask &= data['district'].str.contains(search, case=False, na=False)
    
    st.sidebar.divider()
    st.sidebar.info(f"**Dev Access:** [GitHub Repository](https://github.com/T786-eng/Hackhathon--Project-DRAM--Dynamic-Resource-Allocation-Model-for-Aadhaar-Infrastructure.git)")
    return data[mask]

filtered_df = render_sidebar(df)

# --- 4. MAIN INTERFACE ---
st.title("📊 Project DRAM | Resource Allocation Engine")
st.markdown("##### *Dynamic Infrastructure Analysis for UIDAI Scalability*")

# Metrics Layer
k1, k2, k3, k4 = st.columns(4)
k1.metric("Analytical Scope", f"{len(filtered_df)} Districts")
k2.metric("Critical Nodes", len(filtered_df[filtered_df['Zone_Strategy'].str.contains('RED')]), delta="High Priority", delta_color="inverse")
k3.metric("System UER", f"{summary['Average_UER'].iloc[0]:.2f}", help="Updates-to-Enrolment Ratio")
k4.metric("Transition Forecast", int(summary['Districts_Expected_to_Transition'].iloc[0]), delta="Predicted")

st.divider()

# Visualizations Row
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("🌐 Resource Deployment Hierarchy")
    fig_sun = px.sunburst(
        filtered_df, path=['state', 'Zone_Strategy'], values='Updates',
        color='Zone_Strategy', color_discrete_map=ZONE_COLORS,
        template="plotly_white"
    )
    # Use container width to ensure consistent rendering across browsers
    st.plotly_chart(fig_sun, use_container_width=True)
    
    with st.expander("🔍 View Hierarchy Logic"):
        st.write("""
        **Inner Circle:** State-level aggregation.  
        **Outer Slices:** Strategy Assignment.  
        **Insight:** Identifies 'Update-Heavy' regions requiring permanent infrastructure hubs.
        """)

with col_r:
    st.subheader("📈 Demand & Saturation Analysis")
    fig_scatter = px.scatter(
        filtered_df, x="Enrolments", y="Updates", color="Zone_Strategy", 
        hover_name="district", size="UER", log_x=True, log_y=True,
        color_discrete_map=ZONE_COLORS, template="plotly_white"
    )
    # Use container width to ensure consistent rendering across browsers
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    with st.expander("🔍 View Saturation Logic"):
        st.write("""
        **High Y / Low X:** Indicates 'Saturated' districts.  
        **Pivot:** Resources should shift from new enrolments to biometric maintenance.
        """)

# Data Matrix
st.divider()
st.subheader("📋 Strategic Deployment Matrix")
st.dataframe(
    filtered_df[['state', 'district', 'UER', 'Zone_Strategy', 'Predicted_Trajectory']]
    .sort_values('UER', ascending=False),
    column_config={
        "UER": st.column_config.NumberColumn("UER Ratio", format="%.2f"),
        "Zone_Strategy": "Deployment Strategy",
        "Predicted_Trajectory": "Forecasted Trajectory"
    },
    use_container_width=True,
    hide_index=True
)