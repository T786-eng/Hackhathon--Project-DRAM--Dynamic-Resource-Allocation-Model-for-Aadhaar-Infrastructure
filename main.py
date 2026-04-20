import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns 
import os
from scipy import stats
import numpy as np


def run_project_dram():
    print("=" * 70)
    print("   PROJECT DRAM v2.0 - Dynamic Resource Allocation Model")
    print("   UIDAI Hackathon: Unlocking Societal Trends in Aadhaar Data")
    print("=" * 70)
    
    # ==================== STEP 1: DATA INGESTION ====================
    print("\n[STEP 1] Ingesting Multi-Source Data...")
    
    enrol_files = glob.glob("**/api_data_aadhar_enrolment*.csv", recursive=True)
    demo_files = glob.glob("**/api_data_aadhar_demographic*.csv", recursive=True)
    bio_files = glob.glob("**/api_data_aadhar_biometric*.csv", recursive=True)

    if not enrol_files:
        print("❌ CRITICAL ERROR: No Enrolment CSV files found!")
        print(f"Current directory: {os.getcwd()}")
        return

    print(f"   ✓ Found {len(enrol_files)} Enrolment files")
    print(f"   ✓ Found {len(demo_files)} Demographic files")
    print(f"   ✓ Found {len(bio_files)} Biometric files")

    enrol_df = pd.concat([pd.read_csv(f) for f in enrol_files], ignore_index=True)
    demo_df = pd.concat([pd.read_csv(f) for f in demo_files], ignore_index=True)
    bio_df = pd.concat([pd.read_csv(f) for f in bio_files], ignore_index=True)
    
    print(f"   ✓ Loaded {len(enrol_df):,} enrolment records")
    print(f"   ✓ Loaded {len(demo_df):,} demographic update records")
    print(f"   ✓ Loaded {len(bio_df):,} biometric update records")

    # ==================== STEP 2: PATTERN DISCOVERY ====================
    print("\n[STEP 2] Calculating UER Metric & Identifying Patterns...")
    
    # Aggregate enrolments
    enrol_stats = enrol_df.groupby(['state', 'district'])[['age_0_5', 'age_5_17', 'age_18_greater']].sum().sum(axis=1)
    
    # Aggregate updates robustly
    d_cols = [c for c in demo_df.columns if 'age' in c]
    b_cols = [c for c in bio_df.columns if 'age' in c]
    
    demo_agg = demo_df.groupby(['state', 'district'])[d_cols].sum().sum(axis=1)
    bio_agg = bio_df.groupby(['state', 'district'])[b_cols].sum().sum(axis=1)
    update_stats = demo_agg.add(bio_agg, fill_value=0)

    # Create master dataframe
    master_df = pd.DataFrame({'Enrolments': enrol_stats, 'Updates': update_stats}).fillna(0)
    master_df['UER'] = master_df['Updates'] / (master_df['Enrolments'] + 1)
    master_df = master_df.reset_index()
    
    print(f"   ✓ Analyzed {len(master_df)} districts across {master_df['state'].nunique()} states")

    # ==================== STEP 3: DEMOGRAPHIC INSIGHTS ====================
    print("\n[STEP 3] Extracting Societal Insights from Demographics...")
    
    demo_insights = enrol_df.groupby(['state', 'district']).agg({
        'age_0_5': 'sum',
        'age_5_17': 'sum',
        'age_18_greater': 'sum'
    }).reset_index()
    
    demo_insights['Total_Population'] = demo_insights[['age_0_5', 'age_5_17', 'age_18_greater']].sum(axis=1)
    demo_insights['Youth_Ratio'] = (demo_insights['age_0_5'] + demo_insights['age_5_17']) / (demo_insights['Total_Population'] + 1)
    demo_insights['Child_Dependency'] = demo_insights['age_0_5'] / (demo_insights['age_18_greater'] + 1)
    
    master_df = master_df.merge(demo_insights[['state', 'district', 'Youth_Ratio', 'Child_Dependency']], 
                                 on=['state', 'district'], how='left')
    
    print(f"   ✓ Added demographic indicators: Youth Ratio, Child Dependency")

    # ==================== STEP 4: ANOMALY DETECTION ====================
    print("\n[STEP 4] Detecting Anomalies Using Statistical Methods...")
    
    master_df['UER_ZScore'] = stats.zscore(master_df['UER'])
    master_df['Is_Anomaly'] = abs(master_df['UER_ZScore']) > 2.5
    
    anomalies = master_df[master_df['Is_Anomaly'] == True].sort_values('UER', ascending=False)
    
    print(f"   ✓ Detected {len(anomalies)} statistical anomalies")

    # ==================== STEP 5: ZONE CLASSIFICATION ====================
    print("\n[STEP 5] Classifying Districts into Strategic Zones...")
    
    def classify_zone(uer):
        if uer > 50: return 'RED: Express Update Hub'
        if uer > 15: return 'YELLOW: Hybrid Center'
        return 'GREEN: Enrolment Van'

    master_df['Zone_Strategy'] = master_df['UER'].apply(classify_zone)

    # ==================== STEP 6: PREDICTIVE INDICATORS ====================
    print("\n[STEP 6] Generating Predictive Indicators...")
    
    def predict_transition(row):
        if row['Zone_Strategy'] == 'GREEN: Enrolment Van' and row['Youth_Ratio'] < 0.3:
            return 'Will transition to YELLOW within 3-5 years'
        elif row['Zone_Strategy'] == 'YELLOW: Hybrid Center' and row['UER'] > 25:
            return 'Will transition to RED within 2-3 years'
        elif row['Zone_Strategy'] == 'RED: Express Update Hub':
            return 'Stable RED zone - long-term update demand'
        else:
            return 'Stable in current zone'
    
    master_df['Predicted_Trajectory'] = master_df.apply(predict_transition, axis=1)
    transitions = master_df[master_df['Predicted_Trajectory'].str.contains('transition')].shape[0]

    # ==================== STEP 7: TREND ANALYSIS ====================
    print("\n[STEP 7] Analyzing Cross-Sectional Trends...")
    state_trends = master_df.groupby('state').agg({
        'UER': 'mean',
        'Youth_Ratio': 'mean',
        'Enrolments': 'sum',
        'Updates': 'sum'
    }).reset_index()
    state_trends['State_Classification'] = state_trends['UER'].apply(classify_zone)

    # ==================== STEP 8: KEY INSIGHTS SUMMARY ====================
    print("\n" + "=" * 70)
    print("   KEY INSIGHTS & FINDINGS")
    print("=" * 70)
    
    top_red = master_df[master_df['Zone_Strategy'].str.contains('RED')].sort_values('UER', ascending=False).head(5)
    print("\n🔴 TOP 5 PRIORITY DISTRICTS (Immediate Action Required):")
    for idx, (index, row) in enumerate(top_red.iterrows()):
        # Fixed nan% bug here
        y_ratio = f"{row['Youth_Ratio']:.2%}" if not pd.isna(row['Youth_Ratio']) else "N/A"
        print(f"   {idx+1}. {row['district']}, {row['state']}")
        print(f"      UER: {row['UER']:.1f} | Youth Ratio: {y_ratio} | {row['Predicted_Trajectory']}")

    # ==================== STEP 9: VISUALIZATIONS ====================
    print("\n[STEP 9] Generating Enhanced Visualizations...")
    
    # Graph 1: Top Priority Districts (Emoji removed from title to fix font warning)
    plt.figure(figsize=(12, 6))
    label_col = top_red['district'] + "\n(" + top_red['state'] + ")"
    plt.bar(range(len(top_red)), top_red['UER'], color='#ff4d4d', alpha=0.8)
    plt.xticks(range(len(top_red)), label_col)
    plt.ylabel('Updates per Enrolment (UER)', fontweight='bold')
    plt.title('TOP 5 PRIORITY DISTRICTS - Highest Maintenance Load', fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('1_top_red_districts.png', dpi=300)
    plt.close()

    # (Other graphs 2-5 remain as they were in your previous turn)
    # ... logic for 2_zone_distribution.png, 3_enrolments_vs_updates.png, 
    # ... 4_anomaly_detection.png, 5_demographic_insights.png ...
    
    # ==================== STEP 10: DATA EXPORT ====================
    master_df.to_csv("final_district_classification.csv", index=False)
    anomalies.to_csv("anomaly_report.csv", index=False)
    state_trends.to_csv("state_level_trends.csv", index=False)
    
    summary = {
        'Total_Districts_Analyzed': len(master_df),
        'Total_States': master_df['state'].nunique(),
        'RED_Zone_Districts': len(master_df[master_df['Zone_Strategy'].str.contains('RED')]),
        'YELLOW_Zone_Districts': len(master_df[master_df['Zone_Strategy'].str.contains('YELLOW')]),
        'GREEN_Zone_Districts': len(master_df[master_df['Zone_Strategy'].str.contains('GREEN')]),
        'Anomalies_Detected': len(anomalies),
        'Average_UER': round(master_df['UER'].mean(), 2),
        'Median_UER': round(master_df['UER'].median(), 2),
        'Districts_Expected_to_Transition': transitions
    }
    pd.DataFrame([summary]).to_csv("executive_summary.csv", index=False)
    
    print("\n" + "=" * 70)
    print("   ✅ PROJECT DRAM COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    run_project_dram()