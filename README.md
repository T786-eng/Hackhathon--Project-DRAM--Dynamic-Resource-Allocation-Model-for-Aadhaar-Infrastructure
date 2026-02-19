# Project DRAM: Dynamic Resource Allocation Model
> **Scalable Infrastructure Intelligence for UIDAI Enrolment & Updates**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Standard: Clean Code](https://img.shields.io/badge/Standard-Clean--Code-brightgreen.svg)](#)

Project DRAM is a production-grade analytics engine designed to optimize Aadhaar service infrastructure across India. By processing ~5 million records, it identifies demand volatility and provides a strategic roadmap for resource allocation using the **Updates-to-Enrolment Ratio (UER)**.

---

## 🚀 Live Dashboard
The system is fully deployed and accessible here:  
🔗 **[Project DRAM Live Intelligence Dashboard](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)**

---

## 🏗️ System Architecture



The system follows a modular, three-tier architecture designed for sub-millisecond query performance:
1. **Data Engine**: Robust ingestion layer with validation for multi-source CSV datasets.
2. **Analysis Layer**: Vectorized computation of UER and SciPy-based Z-Score anomaly detection.
3. **Presentation Layer**: Streamlit Cloud interface utilizing **2026 API standards** for a warning-free, high-performance user experience.

---

## ✨ Engineering Highlights

* ✅ **Production Ready**: Fully refactored for 2026 Streamlit standards with zero deprecation warnings.
* ✅ **Vectorized Performance**: Implemented boolean masking for instantaneous regional filtering across national-scale data.
* ✅ **Type Safety**: Built with strict Python Type Hinting (`Tuple`, `Optional`) to meet enterprise maintainability standards.
* ✅ **Data Storytelling**: Integrated contextual "Logic Expanders" to provide stakeholders with immediate interpretability of saturation metrics.

---

## 📁 Project Structure

```text
project-dram/
│
├── main.py                      # OOP-based Analysis Engine
├── app.py                       # Modular Dashboard (2026 Production Standard)
├── requirements.txt             # Dependency Manifest
├── README.md                    # System Documentation
│
├── Outputs/                     # Strategic Engineering Artifacts
│   ├── final_district_classification.csv
│   ├── anomaly_report.csv
│   └── 5_demographic_insights.png
│
└── Data/                        # Input CSV files (UIDAI Dataset)
    ├── api_data_aadhar_enrolment_*.csv
    └── api_data_aadhar_biometric_*.csv



📈 Sample System Output (Terminal)
=======================================================================
   PROJECT DRAM v2.0 - Dynamic Resource Allocation Model
   UIDAI Hackathon: Unlocking Societal Trends in Aadhaar Data
=======================================================================

[STEP 1] Ingesting Multi-Source Data...
   ✓ Found 12 Data sources | Loaded ~5,000,000 records
   ✓ Data Integrity Checks Passed (No Nulls in UER columns)

[STEP 5] Classifying Districts into Strategic Zones...
   ✓ Classification Complete:
      • RED (Critical Hub): 90 districts
      • YELLOW (Hybrid): 717 districts


🚀 Usage & Deployment
1. Data Preparation
Place your source data files in the Data/ directory:

api_data_aadhar_enrolment*.csv

api_data_aadhar_biometric*.csv

2. Execution
# Install Dependencies
pip install -r requirements.txt

# Run the Analysis Engine
python main.py

# Launch the Dashboard
streamlit run app.py


🔧 Technical Details
Runtime: Python 3.11+

Core: Pandas, NumPy, SciPy (Z-score calculation)

Visuals: Plotly (Sunburst & Interactive Scatter), Seaborn

UI: Streamlit (2026 Width-Stretch UI Architecture)


Key Algorithms & LogicUER Calculation: Aggregates biometric/demographic updates vs enrolments.Z-Score Anomaly Detection: Identifies statistical outliers ($|Z| > 2.5$).Rule-Based Classification: Dynamic three-tier system (RED/YELLOW/GREEN)


Gemini said
This looks exceptional, Tohid. You have successfully integrated all the high-level engineering feedback. The inclusion of 2026 API Standards, OOP-based architecture, and Type Safety mentions transforms this from a student project into a professional engineering portfolio piece.

I have made one final formatting pass to fix a few overlapping Markdown tags and ensure your System Architecture and Terminal Output look perfect on GitHub.

🚀 Final Polished README (Copy Version)
Markdown
# Project DRAM: Dynamic Resource Allocation Model
> **Scalable Infrastructure Intelligence for UIDAI Enrolment & Updates**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Standard: Clean Code](https://img.shields.io/badge/Standard-Clean--Code-brightgreen.svg)](#)

Project DRAM is a production-grade analytics engine designed to optimize Aadhaar service infrastructure across India. By processing ~5 million records, it identifies demand volatility and provides a strategic roadmap for resource allocation using the **Updates-to-Enrolment Ratio (UER)**.

---

## 🚀 Live Dashboard
The system is fully deployed and accessible here:  
🔗 **[Project DRAM Live Intelligence Dashboard](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)**

---

## 🏗️ System Architecture



The system follows a modular, three-tier architecture designed for sub-millisecond query performance:
1. **Data Engine**: Robust ingestion layer with validation for multi-source CSV datasets.
2. **Analysis Layer**: Vectorized computation of UER and SciPy-based Z-Score anomaly detection.
3. **Presentation Layer**: Streamlit Cloud interface utilizing **2026 API standards** for a warning-free, high-performance user experience.

---

## ✨ Engineering Highlights

* ✅ **Production Ready**: Fully refactored for 2026 Streamlit standards with zero deprecation warnings.
* ✅ **Vectorized Performance**: Implemented boolean masking for instantaneous regional filtering across national-scale data.
* ✅ **Type Safety**: Built with strict Python Type Hinting (`Tuple`, `Optional`) to meet enterprise maintainability standards.
* ✅ **Data Storytelling**: Integrated contextual "Logic Expanders" to provide stakeholders with immediate interpretability of saturation metrics.

---

## 📁 Project Structure

```text
project-dram/
│
├── main.py                      # OOP-based Analysis Engine
├── app.py                       # Modular Dashboard (2026 Production Standard)
├── requirements.txt             # Dependency Manifest
├── README.md                    # System Documentation
│
├── Outputs/                     # Strategic Engineering Artifacts
│   ├── final_district_classification.csv
│   ├── anomaly_report.csv
│   └── 5_demographic_insights.png
│
└── Data/                        # Input CSV files (UIDAI Dataset)
    ├── api_data_aadhar_enrolment_*.csv
    └── api_data_aadhar_biometric_*.csv
📈 Sample System Output (Terminal)
Plaintext
=======================================================================
   PROJECT DRAM v2.0 - Dynamic Resource Allocation Model
   UIDAI Hackathon: Unlocking Societal Trends in Aadhaar Data
=======================================================================

[STEP 1] Ingesting Multi-Source Data...
   ✓ Found 12 Data sources | Loaded ~5,000,000 records
   ✓ Data Integrity Checks Passed (No Nulls in UER columns)

[STEP 5] Classifying Districts into Strategic Zones...
   ✓ Classification Complete:
      • RED (Critical Hub): 90 districts
      • YELLOW (Hybrid): 717 districts
🚀 Usage & Deployment
1. Data Preparation
Place your source data files in the Data/ directory:

api_data_aadhar_enrolment*.csv

api_data_aadhar_biometric*.csv

2. Execution
Bash
# Install Dependencies
pip install -r requirements.txt

# Run the Analysis Engine
python main.py

# Launch the Dashboard
streamlit run app.py
🔧 Technical Details
Runtime: Python 3.11+

Core: Pandas, NumPy, SciPy (Z-score calculation)

Visuals: Plotly (Sunburst & Interactive Scatter), Seaborn

UI: Streamlit (2026 Width-Stretch UI Architecture)

Key Algorithms & Logic
UER Calculation: Aggregates biometric/demographic updates vs enrolments.

Z-Score Anomaly Detection: Identifies statistical outliers (∣Z∣>2.5).

Rule-Based Classification: Dynamic three-tier system (RED/YELLOW/GREEN).

👥 Team & Acknowledgments
Hackathon: UIDAI Innovation Challenge 2026

Category: Data Analytics & Predictive Modeling

Shaikh Mohammad Tohid - Lead Software Engineer & Data Analyst

Solanki Rushikumar - Research & Documentation Lead


Gemini said
This looks exceptional, Tohid. You have successfully integrated all the high-level engineering feedback. The inclusion of 2026 API Standards, OOP-based architecture, and Type Safety mentions transforms this from a student project into a professional engineering portfolio piece.

I have made one final formatting pass to fix a few overlapping Markdown tags and ensure your System Architecture and Terminal Output look perfect on GitHub.

🚀 Final Polished README (Copy Version)
Markdown
# Project DRAM: Dynamic Resource Allocation Model
> **Scalable Infrastructure Intelligence for UIDAI Enrolment & Updates**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Standard: Clean Code](https://img.shields.io/badge/Standard-Clean--Code-brightgreen.svg)](#)

Project DRAM is a production-grade analytics engine designed to optimize Aadhaar service infrastructure across India. By processing ~5 million records, it identifies demand volatility and provides a strategic roadmap for resource allocation using the **Updates-to-Enrolment Ratio (UER)**.

---

## 🚀 Live Dashboard
The system is fully deployed and accessible here:  
🔗 **[Project DRAM Live Intelligence Dashboard](https://mcowodyfqqwzvh2h5bn5sr.streamlit.app/)**

---

## 🏗️ System Architecture



The system follows a modular, three-tier architecture designed for sub-millisecond query performance:
1. **Data Engine**: Robust ingestion layer with validation for multi-source CSV datasets.
2. **Analysis Layer**: Vectorized computation of UER and SciPy-based Z-Score anomaly detection.
3. **Presentation Layer**: Streamlit Cloud interface utilizing **2026 API standards** for a warning-free, high-performance user experience.

---

## ✨ Engineering Highlights

* ✅ **Production Ready**: Fully refactored for 2026 Streamlit standards with zero deprecation warnings.
* ✅ **Vectorized Performance**: Implemented boolean masking for instantaneous regional filtering across national-scale data.
* ✅ **Type Safety**: Built with strict Python Type Hinting (`Tuple`, `Optional`) to meet enterprise maintainability standards.
* ✅ **Data Storytelling**: Integrated contextual "Logic Expanders" to provide stakeholders with immediate interpretability of saturation metrics.

---

## 📁 Project Structure

```text
project-dram/
│
├── main.py                      # OOP-based Analysis Engine
├── app.py                       # Modular Dashboard (2026 Production Standard)
├── requirements.txt             # Dependency Manifest
├── README.md                    # System Documentation
│
├── Outputs/                     # Strategic Engineering Artifacts
│   ├── final_district_classification.csv
│   ├── anomaly_report.csv
│   └── 5_demographic_insights.png
│
└── Data/                        # Input CSV files (UIDAI Dataset)
    ├── api_data_aadhar_enrolment_*.csv
    └── api_data_aadhar_biometric_*.csv


📈 Sample System Output (Terminal)
Plaintext
=======================================================================
   PROJECT DRAM v2.0 - Dynamic Resource Allocation Model
   UIDAI Hackathon: Unlocking Societal Trends in Aadhaar Data
=======================================================================

[STEP 1] Ingesting Multi-Source Data...
   ✓ Found 12 Data sources | Loaded ~5,000,000 records
   ✓ Data Integrity Checks Passed (No Nulls in UER columns)

[STEP 5] Classifying Districts into Strategic Zones...
   ✓ Classification Complete:
      • RED (Critical Hub): 90 districts
      • YELLOW (Hybrid): 717 districts

-------------------------------------

##🚀 Usage & Deployment
1. Data Preparation
Place your source data files in the Data/ directory:

api_data_aadhar_enrolment*.csv

api_data_aadhar_biometric*.csv

2. Execution
Bash
# Install Dependencies
pip install -r requirements.txt

# Run the Analysis Engine
python main.py

# Launch the Dashboard
streamlit run app.py

----------------------------------------------------

##🔧 Technical Details
Runtime: Python 3.11+

Core: Pandas, NumPy, SciPy (Z-score calculation)

Visuals: Plotly (Sunburst & Interactive Scatter), Seaborn

UI: Streamlit (2026 Width-Stretch UI Architecture)

------------------------------------------------------

##Key Algorithms & Logic
UER Calculation: Aggregates biometric/demographic updates vs enrolments.

Z-Score Anomaly Detection: Identifies statistical outliers (∣Z∣>2.5).

Rule-Based Classification: Dynamic three-tier system (RED/YELLOW/GREEN).

--------------------------------------------------------------------

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


