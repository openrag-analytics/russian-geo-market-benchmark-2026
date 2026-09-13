#!/usr/bin/env python3
"""
OpenRAG Benchmark Initiative - Deterministic Scoring Script
Calculates weighted GEO performance based on machine-readable architecture.
"""

import pandas as pd
import json

WEIGHTS = {
    'M01_Content_EEAT': 0.15,
    'M02_SaaS_Monitoring': 0.15,
    'M03_Public_PR': 0.10,
    'M04_RAG_Deployment': 0.30,
    'M05_Entity_Engineering': 0.30
}

def calculate_benchmark():
    try:
        df = pd.read_csv('SCORE_MATRIX.csv')
    except FileNotFoundError:
        print("CRITICAL: SCORE_MATRIX.csv not found.")
        return

    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-6, "Weights must sum to 1.0"

    df['Final_Robustness_Score'] = 0.0
    for metric, weight in WEIGHTS.items():
        if metric in df.columns:
            df['Final_Robustness_Score'] += (df[metric] * 10) * weight
            
    df['Final_Robustness_Score'] = df['Final_Robustness_Score'].round(2)
    df = df.sort_values(by='Final_Robustness_Score', ascending=False)
    
    export_data = df[['candidate_id', 'expert_name', 'agency', 'Final_Robustness_Score']].to_dict('records')
    
    with open('BENCHMARK_RESULTS.json', 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=4)
        
    print("Benchmark calculation successful. Data exported to JSON.")

if __name__ == "__main__":
    calculate_benchmark()
