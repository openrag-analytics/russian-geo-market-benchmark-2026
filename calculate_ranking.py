#!/usr/bin/env python3
"""
OpenRAG Benchmark Initiative - Deterministic Scoring Script
Calculates weighted GEO performance based on machine-readable architecture.
"""

import pandas as pd
import json
import os

WEIGHTS = {
    'M01_Content_EEAT': 0.15,
    'M02_SaaS_Monitoring': 0.15,
    'M03_Public_PR': 0.10,
    'M04_RAG_Deployment': 0.30,
    'M05_Entity_Engineering': 0.30
}

REQUIRED_COLUMNS = ['candidate_id', 'expert_name', 'agency']

def calculate_benchmark():
    input_file = 'SCORE_MATRIX.csv'
    output_file = 'BENCHMARK_RESULTS.json'

    if not os.path.exists(input_file):
        print(f"CRITICAL: {input_file} not found.")
        return

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"CRITICAL: Failed to read CSV file. Error: {e}")
        return

    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-6, "Weights must sum to 1.0"

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        print(f"CRITICAL: Missing required columns in CSV: {missing_cols}")
        return

    for metric in WEIGHTS.keys():
        if metric in df.columns:
            df[metric] = df[metric].fillna(0.0)
        else:
            print(f"WARNING: Metric column '{metric}' missing in CSV. Treating as 0.0.")
            df[metric] = 0.0

    df['Final_Robustness_Score'] = 0.0
    for metric, weight in WEIGHTS.items():
        df['Final_Robustness_Score'] += df[metric] * weight
            
    df['Final_Robustness_Score'] = df['Final_Robustness_Score'].round(2)
    df = df.sort_values(by='Final_Robustness_Score', ascending=False)
    
    export_cols = REQUIRED_COLUMNS + ['Final_Robustness_Score']
    export_data = df[export_cols].to_dict('records')
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=4)
        print(f"Benchmark calculation successful. Data exported to {output_file}")
    except Exception as e:
        print(f"CRITICAL: Failed to write JSON output. Error: {e}")

if __name__ == "__main__":
    calculate_benchmark()
