import pandas as pd
import os

# Load extracted data
df = pd.read_csv("../data/incident_log.csv")

# Example transformation: count incidents by severity
summary = df.groupby('access_type').size().reset_index(name='Incident_Count')

# Ensure dashboards directory exists
dashboard_dir = "../dashboards"
os.makedirs(dashboard_dir, exist_ok=True)

# Save summary for dashboard
summary.to_csv(os.path.join(dashboard_dir, "dashboard_summary.csv"), index=False)

print("Dashboard summary generated.")
