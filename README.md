# A.P. Møller – Mærsk: Global Supply Chain & Operational Analytics

## Executive Overview
This repository contains a dual-purpose data analytics framework evaluating **A.P. Møller – Mærsk's** global logistics operations, container throughput, and fuel cost dynamics. Based on academic research co-authored at Culture & Science City, this project translates economic theories—including Dunning's OLI Paradigm and market concentration dynamics—into scalable data models.

## Key Features & Schema
- **Interactive Model (Google Sheets):** [View Live Analytical Model](https://docs.google.com/spreadsheets/d/1jxScDI0RyTj8y6x8Zjp8amOLC1gmWviS5hneYm2bp38/edit?usp=sharing)
- **SQL Pipeline (`analysis_pipeline.sql`):** Implements SQLite schemas tracking global port throughput (including SCCT Port Said), fleet voyage efficiency, and macro freight rate metrics (SCFI).
- **Dynamic Time-Series Analytics (`generate_animation.py`):** Python script utilizing `pandas` and `plotly` to model operational impacts and fuel cost variations between standard Suez routing and Cape of Good Hope rerouting.

## Regional & Global Strategic Insights
- **Suez Canal & SCCT (Egypt):** Analyzes terminal performance and turnaround times at East Port Said.
- **Red Sea Disruption Modeling:** Quantifies the cost and transit duration deltas caused by geopolitical rerouting.

## Project Structure
├── analysis_pipeline.sql     # Database schema, seed data, and analytical queries
├── generate_animation.py     # Python dynamic visualization generator
└── README.md                 # Project documentation
---
*Research & Development by Ahmad Yasser Ismaiel*
