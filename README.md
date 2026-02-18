# Project DRAM: Dynamic Resource Allocation Model
> **Unlocking Societal Trends in Aadhaar Enrolment and Updates**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

Project DRAM is a data-driven intelligence solution designed to optimize Aadhaar infrastructure deployment across India. By analyzing millions of transaction records, it identifies demand patterns, detects statistical anomalies, and predicts future resource requirements using the **Updates-to-Enrolment Ratio (UER)**.

---

## 🚀 Live Deployment
Access the interactive intelligence dashboard here:  
🔗 **[Live Dashboard Link](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)**

---

## 🏗️ Project Architecture

```text
┌─────────────────────┐
│    Input Data       │
│   (3 CSV Sources)   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Data Processing    │
│  - Aggregation      │
│  - UER Calculation  │
│  - Demographics     │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│   Analysis Layer    │
│  - Clustering       │
│  - Anomaly Detection│
│  - Predictions      │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  Output Generation  │
│  - 5 Visualizations │
│  - 4 CSV Reports    │
│  - Console Insights │
└─────────────────────┘
## ✨ Key Features

* ✅ **Pattern Discovery**: Identifies three distinct district demand clusters (**Red/Yellow/Green**).
* ✅ **Anomaly Detection**: Statistical outlier flagging using Z-scores to identify system stress.
* ✅ **Demographic Insights**: Deep dive into Youth ratio and child dependency analysis.
* ✅ **Predictive Modeling**: Forecasts zone transitions for long-term strategic planning.
* ✅ **Professional Visualizations**: 5 publication-ready graphs (300 DPI) for reporting.
* ✅ **Comprehensive Reports**: 4 detailed CSV files for stakeholders and administrators.
* ✅ **Scalable**: Optimized to handle national-scale datasets with millions of rows.

## 🚀 Usage & Deployment

### Data Preparation
Place your source data files in the project directory (or any subfolder):
* `api_data_aadhar_enrolment*.csv`
* `api_data_aadhar_demographic*.csv`
* `api_data_aadhar_biometric*.csv`

### Execution
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Analysis:**
   ```bash
   python main.py
   ```

3. **Launch the Dashboard:**
   ```bash
   streamlit run app.py
   ```

Check Outputs
* 📊 5 PNG visualizations in the root directory.

* 📁 4 CSV reports (final_district_classification.csv, anomaly_report.csv, etc.).

* 🖥️ Console output with live key findings and infrastructure gap analysis.


📁 Project Structure:
project-dram/
│
├── main.py                      # Main analysis engine
├── app.py                       # Streamlit Dashboard script
├── requirements.txt             # Python dependencies
├── README.md                    # Project Documentation
│
├── Outputs/                     # Generated files
│   ├── 1_top_red_districts.png
│   ├── 2_zone_distribution.png
│   ├── 3_enrolments_vs_updates.png
│   ├── 4_anomaly_detection.png
│   ├── 5_demographic_insights.png
│   ├── final_district_classification.csv
│   ├── anomaly_report.csv
│   ├── state_level_trends.csv
│   └── executive_summary.csv
│
└── Data/                        # Input CSV files (UIDAI Dataset)
    ├── api_data_aadhar_enrolment_*.csv
    ├── api_data_aadhar_demographic_*.csv
    └── api_data_aadhar_biometric_*.csv


📈 Sample Findings (Console Output):
=======================================================================
   PROJECT DRAM v2.0 - Dynamic Resource Allocation Model
   UIDAI Hackathon: Unlocking Societal Trends in Aadhaar Data
=======================================================================

[STEP 1] Ingesting Multi-Source Data...
   ✓ Found 12 Data sources | Loaded ~5,000,000 records
   
[STEP 5] Classifying Districts into Strategic Zones...
   ✓ Classification Complete:
      • RED (High Priority): 90 districts
      • YELLOW (Balanced): 717 districts
      • GREEN (Enrolment): 325 districts

🔴 TOP 5 PRIORITY DISTRICTS (Critical Action Required):
   1. Khairthal-Tijara, Rajasthan (UER: 1072.0)
   2. Kotputli-Behror, Rajasthan (UER: 536.0)
   [...]


## 🔧 Technical Details

* **Language**: Python 3.11+
* **Data Processing**: Pandas, NumPy
* **Statistical Analysis**: SciPy (Z-score calculations)
* **Visualization**: Plotly, Matplotlib, Seaborn
* **Deployment**: Streamlit Community Cloud

### Key Algorithms & Logic
* **UER Calculation**: Aggregates biometric/demographic updates vs enrolments.
* **Z-Score Anomaly Detection**: Identifies statistical outliers (|Z| > 2.5).
* **Rule-Based Classification**: Dynamic three-tier system (RED/YELLOW/GREEN).
* **Predictive Logic**: Forecasts zone transitions based on current Youth Ratio and UER growth.



## 📚 Documentation

- 📄 **Full Documentation**: [## Project Documentation
Click below to view the full project report and technical methodology:

[📄 View Full Project DRAM Documentation](./Project-DRAM-Dynamic-Resource-Allocation-Model-UIDAI-Hackathon-2026.pdf)](docs/DRAM_Documentation.pdf)
- 📊 **Methodology**: Detailed explanation of UER metric and classification logic
- 🎓 **Use Cases**: Infrastructure planning, budget allocation, capacity forecasting

---

## 🤝 Contributing

This is a hackathon submission project. Feedback and suggestions are welcome!

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

**Project**: DRAM (Dynamic Resource Allocation Model)  
**Hackathon**: UIDAI Innovation Challenge 2026  
**Category**: Data Analytics & Predictive Modeling

**Team Members**:
- [Shaikh Mohammad Tohid] - Lead Developer & Data Analyst - [shaikhtohid921@gmail.com]
- [Solanki Rushikumar] - Research & Documentation Lead - [solankirushi75@gmail.com]


---

## 🙏 Acknowledgments

- **UIDAI** for providing the hackathon opportunity and inspiring data-driven governance.
- **Digital** India Initiative for the vision of technology-enabled public services.
- **Open Source Community** for the excellent Python libraries used.

---

## 📧 Contact

For questions, suggestions, or collaboration opportunities:

- 📧 Email: [shaikhtohid921@gmail.com]
- 🔗 LinkedIn: [www.linkedin.com/in/shaikh-tohid]

---

## 🌟 Star This Repository

If you find this project useful or interesting, please consider giving it a ⭐ star on GitHub!

---

