import sqlite3
import pandas as pd
import plotly.express as px

# 1. Connect to SQLite (or create an in-memory database with our sample data)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Execute schema creation & seed data (simulating your GitHub pipeline)
cursor.execute("""
CREATE TABLE fleet_voyages (
    voyage_id TEXT PRIMARY KEY,
    vessel_class TEXT NOT NULL,
    route_name TEXT NOT NULL,
    routing_type TEXT NOT NULL,
    transit_duration_days INTEGER,
    bunker_fuel_consumed_tons REAL,
    co2_emissions_tons REAL,
    fuel_cost_usd REAL,
    disruption_flag BOOLEAN DEFAULT 0,
    year INTEGER
);
""")

# Insert multi-year simulation data for animation
sample_data = [
    ('V001', 'Triple-E', 'Asia-Europe', 'Standard (Suez)', 30, 850.5, 2680.0, 520000.0, 0, 2021),
    ('V002', 'Triple-E', 'Asia-Europe', 'Standard (Suez)', 30, 860.0, 2690.0, 530000.0, 0, 2022),
    ('V003', 'Triple-E', 'Asia-Europe', 'Rerouted (Cape)', 42, 1190.2, 3750.0, 740000.0, 1, 2023),
    ('V004', 'Triple-E', 'Asia-Europe', 'Rerouted (Cape)', 43, 1210.0, 3800.0, 760000.0, 1, 2024),
    ('V005', 'Triple-E', 'Asia-Europe', 'Rerouted (Cape)', 42, 1195.0, 3760.0, 750000.0, 1, 2025),
    ('V006', 'Triple-E', 'Asia-Europe', 'Rerouted (Cape)', 42, 1190.0, 3750.0, 745000.0, 1, 2026)
]
cursor.executemany("INSERT INTO fleet_voyages VALUES (?,?,?,?,?,?,?,?,?,?)", sample_data)
conn.commit()

# 2. Query data into a Pandas DataFrame
df = pd.read_sql("SELECT year, routing_type, fuel_cost_usd, transit_duration_days FROM fleet_voyages", conn)

# 3. Create the Animated Time-Series Chart using Plotly
fig = px.bar(
    df, 
    x='routing_type', 
    y='fuel_cost_usd', 
    animation_frame='year', 
    color='routing_type',
    range_y=[0, 900000],
    title='Mærsk Voyage Cost Impact: Suez vs. Cape of Good Hope (2021-2026)',
    labels={'fuel_cost_usd': 'Fuel Cost (USD)', 'routing_type': 'Routing Strategy'}
)

fig.update_layout(template='plotly_dark', title_font_size=16)
fig.show()
