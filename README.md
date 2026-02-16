# The 2026 Refinancing Wall - Research Report Package

**CEDX Research Report | RR-CEDX-2026-013**

---

## Package Contents

### 📄 Folder 1: Complete_Report
Contains the full research report in DOCX format:
- `The_2026_Refinancing_Wall_Report.docx` - Complete 15,000+ word report with all chapters, figures, tables, and references

### 💻 Folder 2: Code_Files
Contains all code used to generate figures and the report:

**Python Files:**
- `figure_generation_code.py` - Complete Python script to generate all 22 figures
- `generate_figures.py` - Alternative figure generation script

**JavaScript Files:**
- `generate_report.js` - docx-js script to generate the complete DOCX report

### 📊 Folder 3: Images_and_Data
Contains all visual assets and data:

**Figures (22 PNG files at 300 DPI):**
- `figures/` - All charts, graphs, and visualizations
  - Figure 1.1: Conceptual Framework
  - Figure 2.1: Global Interest Rate Trends
  - Figure 2.2: Sovereign Spread Evolution
  - Figure 4.1-4.8: Maturity and Financing Analysis
  - Figure 5.1-5.2: Decision Trees and Feedback Loops
  - Figure 6.1-6.4: Country Case Studies
  - Figure 7.1-7.4: Policy Recommendations
  - Figure 8.1: Risk Heat Map

**Data Tables (9 CSV files):**
- `data/`
  - table_2_1_baseline_indicators.csv
  - table_4_1_maturity_profile.csv
  - table_4_2_gross_financing_needs.csv
  - table_4_3_debt_service_revenue.csv
  - table_4_4_refinancing_gap.csv
  - table_4_5_reserve_adequacy.csv
  - table_6_case_studies.csv
  - table_7_recommendations.csv
  - table_8_risk_register.csv

**Logo:**
- `logo.png` - CEDX logo

---

## How to Regenerate Figures

1. Install requirements: `pip install matplotlib numpy pandas`
2. Run: `python figure_generation_code.py`
3. All figures will be saved to the `figures/` directory

## How to Regenerate the Report

1. Install bun: `curl -fsSL https://bun.sh/install | bash`
2. Install docx: `bun add docx`
3. Run: `bun run generate_report.js`
4. The DOCX file will be generated

---

## Report Summary

**Title:** The 2026 Refinancing Wall: Sovereign Debt Rollover Risks and Crisis Prevention in Emerging Markets

**Key Findings:**
1. Aggregate maturities exceed $70 billion in 2026 alone
2. Four countries exceed the 20% GFN crisis threshold
3. Debt service/revenue ratios exceed 30% in multiple countries
4. FX reserves below 3 months imports in 3 countries
5. Significant refinancing gaps under stress scenarios
6. Sovereign-corporate feedback loop amplifies risks
7. Early engagement produces better outcomes
8. Preventive liability management offers advantages

**Case Studies:**
- Ghana: Eurobond Maturity Challenge
- Sri Lanka: Post-Default Restructuring
- Zambia: Common Framework Pioneer
- Pakistan: Chronic External Imbalance

**Authors:** CEDX Research & Analysis Wing
**Date:** January 2026
**Report Number:** RR-CEDX-2026-013

---

© 2026 Centre for Economic Development and Execution (CEDX)
