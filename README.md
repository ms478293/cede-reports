# The 2026 Refinancing Wall - Research Report Package

**CEDX Research Report | RR-CEDX-2026-013**

---

## Package Contents

### 📄 1_Complete_Report
Contains the full research report:
- `The_2026_Refinancing_Wall_Report.docx` - Complete professional report

### 💻 2_Code_Files
Contains all code used to generate figures and report:
- `figure_generation_code.py` - Python script to generate all 17 figures
- `generate_report.js` - JavaScript script to generate the DOCX report

### 📊 3_Images_and_Data
Contains all visual assets and data:
- `figures/` - 17 PNG figures at 300 DPI
- `data/` - 9 CSV data tables
- `logo.png` - CEDX logo

---

## How to Regenerate Figures

```bash
pip install matplotlib numpy pandas
python 2_Code_Files/figure_generation_code.py
```

## How to Regenerate the Report

```bash
bun add docx
bun run 2_Code_Files/generate_report.js
```

---

## Report Structure

1. Executive Summary
2. Introduction
3. The Global Context
4. Maturity Profile Analysis
5. Stress Scenario Analysis
6. Reserve Adequacy Assessment
7. Case Studies (Ghana, Sri Lanka, Zambia, Pakistan)
8. Counterarguments and Thresholds
9. Recommendations
10. Risk Management Framework
11. Conclusion
12. References

---

© 2026 Centre for Economic Development and Execution (CEDX)
