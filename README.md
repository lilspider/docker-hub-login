# ETL Pipeline

Basic ETL pipeline with Python and DBT.

## Setup
```bash
pip install -r requirements.txt
pip install dbt-core dbt-duckdb
```

## Run
```bash
python etl.py
pytest
dbt run
dbt test
```

## Structure
- `etl.py` - ETL script
- `tests/` - Pytest tests
- `models/` - DBT models
- `data/` - Input data
- `output/` - Output files
