-- =========================================================================
-- Project: A.P. Møller – Mærsk Global Supply Chain & Operational Analytics
-- Database: SQLite 3
-- Author: Ahmad Yasser Morsy
-- =========================================================================

-- Enable foreign key support
PRAGMA foreign_keys = ON;

-- 1. Table: Global Ports & Terminal Throughput (Tracking APM Terminals & SCCT)
CREATE TABLE port_throughput (
    port_id TEXT PRIMARY KEY,
    port_name TEXT NOT NULL,
    region TEXT NOT NULL,
    country TEXT NOT NULL,
    annual_teu_capacity INTEGER,
    average_dwell_time_days REAL,
    berth_occupancy_rate REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Table: Fleet Voyages & Red Sea Disruption Metrics (Cape of Good Hope vs. Suez Canal)
CREATE TABLE fleet_voyages (
    voyage_id TEXT PRIMARY KEY,
    vessel_class TEXT NOT NULL, -- e.g., 'Triple-E', 'Post-Panamax'
    route_name TEXT NOT NULL,    -- e.g., 'Asia-North Europe'
    routing_type TEXT NOT NULL,  -- 'Standard (Suez)' or 'Rerouted (Cape of Good Hope)'
    transit_duration_days INTEGER,
    bunker_fuel_consumed_tons REAL,
    co2_emissions_tons REAL,
    fuel_cost_usd REAL,
    disruption_flag BOOLEAN DEFAULT 0
);

-- 3. Table: Financial, Freight Rates, & Macro Market Indices
CREATE TABLE financial_market_metrics (
    record_date DATE PRIMARY KEY,
    scfi_index_value REAL,        -- Shanghai Containerized Freight Index
    bunker_fuel_price_per_ton REAL, -- HSFO / VLSFO market price
    average_freight_rate_per_teu REAL,
    operating_profit_margin_pct REAL,
    global_gdp_growth_rate REAL
);

-- =========================================================================
-- Sample Seed Data to Test the Pipeline
-- =========================================================================

INSERT INTO port_throughput VALUES 
('EGPSD', 'Port Said East (SCCT)', 'Middle East & Africa', 'Egypt', 5500000, 1.2, 0.78),
('NLRTM', 'Port of Rotterdam', 'Europe', 'Netherlands', 15300000, 1.8, 0.82),
('SGSIN', 'Port of Singapore', 'Asia', 'Singapore', 37300000, 1.0, 0.85);

INSERT INTO fleet_voyages VALUES 
('V001', 'Triple-E', 'Asia-North Europe', 'Standard (Suez)', 30, 850.5, 2680.0, 520000.0, 0),
('V002', 'Triple-E', 'Asia-North Europe', 'Rerouted (Cape of Good Hope)', 42, 1190.2, 3750.0, 740000.0, 1);

INSERT INTO financial_market_metrics VALUES 
('2026-06-30', 2150.4, 620.0, 3100.0, 18.5, 2.8);
