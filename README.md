# Main Roads Integrity Analytics Demonstration

This repository demonstrates an end-to-end integrity analytics pipeline designed for public sector applications such as internal audit, incident risk reporting, and stakeholder dashboarding. The project simulates a real-world data pipeline using Python, SQL, and Power BI-compatible outputs.

🔍 This project was created to support my application for the Integrity Analytics Coordinator position at Main Roads WA (May 2025), and highlights my technical capabilities in ETL design, data governance, audit traceability, and cross-functional insight generation.

## Key Features

- Structured ETL pipeline using Python (Pandas, SQLAlchemy)
- Simulated audit event log (`incident_log.csv`)
- Data cleaning and access-level tagging logic
- Version control and audit trail using JSON
- Output-ready datasets for Power BI or matplotlib dashboards
- Modular script design: `extract.py`, `transform.py`, `load.py`

## Technical Stack

- Python 3.10
- Pandas, NumPy
- SQLAlchemy + SQLite
- Matplotlib
- Power BI (optional export)

## File Structure

```
mainroads-integrity-demo/
├── data/                # Raw input data (e.g., incident_log.csv)
├── scripts/             # Modular ETL scripts
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── dashboards/          # Optional Power BI or matplotlib outputs
├── audit_log/           # Audit trail metadata (e.g., version_log.json)
└── README.md            # Project overview and purpose
```

## Example Use Cases

- Detecting excessive access to sensitive data areas (e.g., repeated logins)
- Flagging unusual time-based or role-inconsistent access patterns
- Supporting integrity monitoring and ethical risk reporting across departments
- Providing data traceability for internal reviews and external audits

---

This demonstration highlights core capabilities aligned with public sector analytics responsibilities: data reliability, ethical transparency, and risk-informed reporting. I welcome further opportunities to apply these methods within an organisational integrity and governance context.
