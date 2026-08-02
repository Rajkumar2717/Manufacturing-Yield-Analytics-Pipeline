---
### **Repository 2: `Manufacturing-Yield-Analytics-Pipeline`**
```markdown
# Manufacturing Test Log Parser & Yield Analytics Engine

## 📌 Overview
An end-to-end Python data pipeline engineered to ingest, parse, and analyze high-volume parametric test log data from simulated manufacturing runs. This tool performs Exploratory Data Analysis (EDA) to identify yield drop drivers, track component failure patterns, and flag parametric out-of-spec conditions, ultimately exporting clean data to a SQL database for dashboard visualization.

## 🚀 Key Features
* **High-Volume Log Parsing:** Uses Pandas and NumPy to efficiently ingest and clean large datasets (simulated as CSV logs), handling missing or corrupted data entries.
* **Parametric Anomaly Detection:** Evaluates test metrics (e.g., 3.3V power rails, temperature limits) against defined manufacturing tolerances.
* **Yield Analytics:** Calculates overall manufacturing yield rates and breaks down the root causes of board failures.
* **SQL Database Integration:** Automatically exports the structured, cleaned parametric data into a local SQLite database, preparing it for real-time tracking in tools like Power BI.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Database:** SQLite3

## ⚙️ How to Run
1. Clone this repository to your local machine.
2. Install the required data science libraries:
   ```bash
   pip install pandas numpy
