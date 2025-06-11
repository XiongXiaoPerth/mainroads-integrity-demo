# Main Roads Integrity Demo

This is a demonstration repository created for the Main Roads WA Integrity Analytics Coordinator application.

The purpose is to provide an example of:
- Basic ETL (Extract-Transform-Load) scripting to process integrity-related data
- Simple audit traceability for version control
- Dashboard-ready reporting outputs for data validation and monitoring

**Disclaimer:** This repository is a simulated demonstration using mock data and simplified scripts.

## Components

- `data/incident_log.csv`: Sample raw data (simulated incident records)
- `scripts/extract.py`: Simulated data extraction script
- `scripts/transform.py`: Example transformation script to clean and summarize data
- `scripts/load.py`: Example load script to generate dashboard-ready summary
- `audit_log/version_log.json`: Example audit log with version traceability
- `dashboard_summary.csv`: Example summary file ready for Power BI/Tableau/dashboard tools

## Example Workflow

```bash
python extract.py
python transform.py
python load.py
