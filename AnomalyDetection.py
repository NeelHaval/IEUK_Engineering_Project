# Import statement
import pandas as pd

# Read the csv data file and create a date and time object
data = pd.read_csv("telemetry_data.csv", parse_dates = ["timestamp"])

# Group turbines by ID
groups = data.groupby("turbine_id")

# Calculate mean temperature for each group
temp_average = groups["temperature_c"].mean()

# Calculate the maximum vibration data point for each turbine
max_vib = groups["vibration_mm_s"].max()

# Create boolean condition to filter out broken turbines
broken = (temp_average > 85) | (max_vib > 15)

# Check through each turbine group for anomaly conditions highlighted in brief
maintenance_required = broken[broken].index.tolist()

# Present final result to show turbines which require maintencance
print("Critical Maintenance Required:\n")
for i in maintenance_required:
    print(f"- {i}")