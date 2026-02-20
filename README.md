# Docker Hub Login with GitHub Actions

This repository demonstrates how to log into Docker Hub using GitHub Actions and secrets.

## 🔧 Setup Required

### 1. Create Docker Hub Access Token
1. Go to [Docker Hub](https://hub.docker.com/)
2. Click your profile → **Account Settings**
3. Go to **Security** tab
4. Click **New Access Token**
5. Give it a name (e.g., "github-actions")
6. Copy the generated token

## 📁 Project Structure

```
├── data/
│   └── input.csv          # Source data file
├── output/                # Generated output files
│   ├── transformed_data.csv
│   └── transformed_data.json
├── etl.py                 # Main ETL script
├── requirements.txt       # Python dependencies
└── .github/workflows/
    └── etl-pipeline.yml   # GitHub Actions workflow
```

## 🔄 ETL Process

### Extract
- Reads employee data from `data/input.csv`
- Loads 10 sample records with employee information

### Transform
- Adds `salary_category` (High/Medium/Low based on salary)
- Adds `age_group` (Senior/Mid/Junior based on age)
- Formats names to title case
- Adds processing timestamp

### Load
- Saves transformed data to `output/transformed_data.csv`
- Saves structured data with metadata to `output/transformed_data.json`

## 🤖 GitHub Actions

The workflow triggers on:
- **Push** to master branch
- **Pull requests** to master branch
- **Manual dispatch** (run manually)
- **Daily schedule** at 2:00 AM UTC

**Features:**
- Runs on Ubuntu latest
- Uses Python 3.11
- Installs dependencies automatically
- Uploads output artifacts
- Displays execution summary

## 🛠️ Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the ETL pipeline:
   ```bash
   python etl.py
   ```

3. Run tests:
   ```bash
   pytest
   # or for verbose output
   pytest -v
   ```

4. Check the output in the `output/` directory

## 🧪 Testing

The project includes comprehensive pytest tests covering:

- **Unit Tests**: Individual function testing
  - `test_extract()` - Data extraction validation
  - `test_transform()` - Data transformation logic
  - `test_load_csv()` - CSV output verification
  - `test_load_json()` - JSON output verification

- **Integration Tests**: End-to-end pipeline testing
  - `test_full_pipeline_integration()` - Complete ETL flow
  - `test_data_integrity()` - Data preservation through pipeline

- **Edge Case Tests**: Boundary conditions
  - `test_edge_cases()` - Empty DataFrame handling
  - `test_salary_categorization()` - Salary boundary testing
  - `test_age_grouping()` - Age boundary testing

**Test Coverage:**
- ✅ Data extraction from CSV
- ✅ Data transformation logic
- ✅ Salary categorization (High/Medium/Low)
- ✅ Age grouping (Senior/Mid/Junior)
- ✅ Name formatting (title case)
- ✅ Output file generation (CSV & JSON)
- ✅ Data integrity preservation
- ✅ Error handling and edge cases

## 📊 Sample Output

The pipeline generates:
- **CSV**: Clean, transformed data ready for analysis
- **JSON**: Structured data with metadata including:
  - Total record count
  - Processing timestamp
  - Column information
  - All transformed records

## 🔧 Next Steps

Extend this ETL pipeline by:
- Adding data validation steps
- Connecting to real data sources (databases, APIs)
- Implementing error handling and logging
- Adding data quality checks
- Connecting to cloud storage (S3, GCS)
- Adding notification systems
