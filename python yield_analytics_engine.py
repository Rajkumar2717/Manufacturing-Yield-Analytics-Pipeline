$ python yield_analytics_engine.py
Generated simulated manufacturing logs: raw_manufacturing_logs.csv

--- Starting Data Ingestion & Parsing ---
Cleaned corrupted data. Rows analyzed: 994/1000

--- Yield Analytics Report ---
Total Boards Tested: 994
Failed Boards: 137
Current Manufacturing Yield: 86.21%

Root Cause Breakdown -> Voltage Fails: 129 | Temp Fails: 14

Data successfully parsed and exported to SQL Database: yield_analytics.db
