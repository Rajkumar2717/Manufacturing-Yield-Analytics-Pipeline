"""
Manufacturing Test Log Parser & Yield Analytics Engine
Parses high-volume parametric test data, performs EDA, and exports to SQL.
"""

import pandas as pd
import numpy as np
import sqlite3
import os

# --- 1. Dummy Data Generator (Simulating Manufacturing Logs) ---
def generate_dummy_logs(filename="raw_manufacturing_logs.csv"):
    """Generates a CSV of simulated hardware test logs."""
    np.random.seed(42)
    num_boards = 1000
    
    data = {
        'board_serial': [f"SN-{10000 + i}" for i in range(num_boards)],
        'test_timestamp': pd.date_range(start='2026-08-01', periods=num_boards, freq='T'),
        'voltage_3v3': np.random.normal(loc=3.3, scale=0.1, size=num_boards), # Simulated 3.3V rail
        'temp_celsius': np.random.normal(loc=45.0, scale=5.0, size=num_boards),
        'boot_time_ms': np.random.randint(200, 500, size=num_boards)
    }
    
    df = pd.DataFrame(data)
    # Inject some random NaN values to simulate corrupted test logs
    df.loc[10:15, 'voltage_3v3'] = np.nan 
    df.to_csv(filename, index=False)
    print(f"Generated simulated manufacturing logs: {filename}")
    return filename

# --- 2. Log Parser & Yield Analytics Engine ---
def process_test_logs(file_path, db_name="yield_analytics.db"):
    print("\n--- Starting Data Ingestion & Parsing ---")
    
    # Ingest Data
    df = pd.read_csv(file_path)
    initial_count = len(df)
    
    # Data Cleaning (Remove corrupted logs)
    df = df.dropna(subset=['voltage_3v3', 'temp_celsius'])
    cleaned_count = len(df)
    print(f"Cleaned corrupted data. Rows analyzed: {cleaned_count}/{initial_count}")
    
    # Exploratory Data Analysis & Anomaly Detection
    # Specifications: 3.3V rail must be between 3.15V and 3.45V
    df['voltage_status'] = np.where(df['voltage_3v3'].between(3.15, 3.45), 'PASS', 'FAIL')
    
    # Specifications: Temp must be under 55C
    df['temp_status'] = np.where(df['temp_celsius'] <= 55.0, 'PASS', 'FAIL')
    
    # Overall Board Status
    df['overall_status'] = np.where((df['voltage_status'] == 'PASS') & (df['temp_status'] == 'PASS'), 'PASS', 'FAIL')
    
    # Yield Analytics Calculations
    failed_boards = len(df[df['overall_status'] == 'FAIL'])
    yield_rate = ((cleaned_count - failed_boards) / cleaned_count) * 100
    
    print("\n--- Yield Analytics Report ---")
    print(f"Total Boards Tested: {cleaned_count}")
    print(f"Failed Boards: {failed_boards}")
    print(f"Current Manufacturing Yield: {yield_rate:.2f}%\n")
    
    # Identify Yield Drop Drivers (Root Cause Analysis)
    voltage_fails = len(df[df['voltage_status'] == 'FAIL'])
    temp_fails = len(df[df['temp_status'] == 'FAIL'])
    print(f"Root Cause Breakdown -> Voltage Fails: {voltage_fails} | Temp Fails: {temp_fails}")

    # --- 3. Export to SQL Database ---
    conn = sqlite3.connect(db_name)
    df.to_sql('parametric_test_data', conn, if_exists='replace', index=False)
    conn.close()
    print(f"\nData successfully parsed and exported to SQL Database: {db_name}")

if __name__ == "__main__":
    log_file = generate_dummy_logs()
    process_test_logs(log_file)
