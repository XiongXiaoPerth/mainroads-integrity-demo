import pandas as pd

# Simulate extraction step
df = pd.read_csv("../data/incident_log.csv")
print(f"Extracted {len(df)} records.")

df.to_csv("../data/temp_extracted.csv", index=False)