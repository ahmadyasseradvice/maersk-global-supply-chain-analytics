import pandas as pd
import plotly.express as px

# Multi-year operational data tracing fuel costs across time
data = [
    {"Year": 2021, "Routing Strategy": "Standard (Suez Canal)", "Fuel Cost (USD)": 520000},
    {"Year": 2022, "Routing Strategy": "Standard (Suez Canal)", "Fuel Cost (USD)": 535000},
    {"Year": 2023, "Routing Strategy": "Rerouted (Cape of Good Hope)", "Fuel Cost (USD)": 745000},
    {"Year": 2024, "Routing Strategy": "Rerouted (Cape of Good Hope)", "Fuel Cost (USD)": 765000},
    {"Year": 2025, "Routing Strategy": "Rerouted (Cape of Good Hope)", "Fuel Cost (USD)": 750000},
    {"Year": 2026, "Routing Strategy": "Rerouted (Cape of Good Hope)", "Fuel Cost (USD)": 745000}
]

df = pd.DataFrame(data)

# Create animated line plot matching time-series race style
fig = px.line(
    df,
    x="Year",
    y="Fuel Cost (USD)",
    color="Routing Strategy",
    markers=True,
    title="Mærsk Voyage Cost Trajectory (2021–2026): Red Sea Rerouting Impact",
    labels={"Fuel Cost (USD)": "Fuel Cost ($)", "Year": "Timeline"}
)

fig.update_layout(template="plotly_dark")
fig.write_html("animated_chart.html")
print("Saved animated chart as animated_chart.html")
