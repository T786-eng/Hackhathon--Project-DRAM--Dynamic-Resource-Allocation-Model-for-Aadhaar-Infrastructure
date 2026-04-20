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
    /* Consistent light blue card for all themes */
    .stMetric {
        background: #e3f0fc;
        color: #23272f !important;
        padding: 18px 15px 15px 15px;
        border-radius: 14px;
        border-left: 6px solid #1976d2;
        box-shadow: 0 2px 8px rgba(0,0,0,0.10);
        margin-bottom: 8px;
        transition: background 0.2s, color 0.2s;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1976d2 !important;
        letter-spacing: 0.5px;
        transition: color 0.2s;
    }
    [data-testid="stMetricValue"] {
        font-size: 2.1rem;
        font-weight: bold;
        color: #23272f !important;
        margin-bottom: 6px;
        transition: color 0.2s;
    }
    .badge-custom {
        display: inline-block;
        padding: 2px 12px;
        border-radius: 12px;
        font-size: 0.95rem;
        font-weight: 700;
        margin-left: 8px;
        vertical-align: middle;
        background: #1976d2;
        color: #fff;
    }
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


# Metrics Layer: all blocks with light blue background
k1, k2, k3, k4 = st.columns(4)
k1.markdown(f"""
    <div class='stMetric'>
        <div data-testid='stMetricLabel'>Analytical Scope</div>
        <div data-testid='stMetricValue'>{len(filtered_df)} Districts</div>
    </div>
    """, unsafe_allow_html=True)
k2.markdown(f"""
    <div class='stMetric'>
        <div style='display: flex; align-items: center;'>
            <span data-testid='stMetricValue'>{len(filtered_df[filtered_df['Zone_Strategy'].str.contains('RED')])}</span>
            <span class='badge-custom'>High Priority</span>
        </div>
        <div data-testid='stMetricLabel'>Critical Nodes</div>
    </div>
    """, unsafe_allow_html=True)
k3.markdown(f"""
    <div class='stMetric'>
        <div data-testid='stMetricLabel'>System UER <span title='Updates-to-Enrolment Ratio' style='cursor: help;'>?</span></div>
        <div data-testid='stMetricValue'>{summary['Average_UER'].iloc[0]:.2f}</div>
    </div>
    """, unsafe_allow_html=True)
k4.markdown(f"""
    <div class='stMetric'>
        <div style='display: flex; align-items: center;'>
            <span data-testid='stMetricValue'>{int(summary['Districts_Expected_to_Transition'].iloc[0])}</span>
            <span class='badge-custom'>Predicted</span>
        </div>
        <div data-testid='stMetricLabel'>Transition Forecast</div>
    </div>
    """, unsafe_allow_html=True)

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
    # Use Streamlit width API ('stretch' for full-width) to avoid deprecation warnings
    st.plotly_chart(fig_sun, width='stretch')
    
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
    # Use Streamlit width API ('stretch' for full-width) to avoid deprecation warnings
    st.plotly_chart(fig_scatter, width='stretch')
    
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
    width='stretch',
    hide_index=True
)