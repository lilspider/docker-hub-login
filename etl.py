#!/usr/bin/env python3

import pandas as pd
import json
from datetime import datetime
import os

def extract():
    """Extract data from CSV file"""
    print("Extracting data from CSV...")
    df = pd.read_csv('data/input.csv')
    print(f"Extracted {len(df)} records")
    return df

def transform(df):
    """Transform the data"""
    print("Transforming data...")
    
    # Add salary category
    df['salary_category'] = df['salary'].apply(
        lambda x: 'High' if x >= 80000 else 'Medium' if x >= 60000 else 'Low'
    )
    
    # Add age group
    df['age_group'] = df['age'].apply(
        lambda x: 'Senior' if x >= 40 else 'Mid' if x >= 30 else 'Junior'
    )
    
    # Format names to title case
    df['name'] = df['name'].str.title()
    
    # Add processing timestamp
    df['processed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Select and reorder columns
    df = df[['id', 'name', 'age', 'age_group', 'city', 'salary', 'salary_category', 'processed_at']]
    
    print(f"Transformed data with new columns: salary_category, age_group")
    return df

def load_csv(df):
    """Load transformed data to CSV"""
    print("Loading data to CSV...")
    os.makedirs('output', exist_ok=True)
    df.to_csv('output/transformed_data.csv', index=False)
    print("Data loaded to output/transformed_data.csv")

def load_json(df):
    """Load transformed data to JSON"""
    print("Loading data to JSON...")
    os.makedirs('output', exist_ok=True)
    
    # Convert to JSON
    json_data = {
        'metadata': {
            'total_records': len(df),
            'processed_at': datetime.now().isoformat(),
            'columns': list(df.columns)
        },
        'data': df.to_dict('records')
    }
    
    with open('output/transformed_data.json', 'w') as f:
        json.dump(json_data, f, indent=2)
    
    print("Data loaded to output/transformed_data.json")

def main():
    """Main ETL pipeline"""
    print("Starting ETL Pipeline...")
    print("=" * 50)
    
    try:
        # Extract
        df = extract()
        
        # Transform
        transformed_df = transform(df)
        
        # Load
        load_csv(transformed_df)
        load_json(transformed_df)
        
        print("=" * 50)
        print("ETL Pipeline completed successfully!")
        print(f"Processed {len(transformed_df)} records")
        print("Output files created in 'output' directory")
        
        # Show sample of transformed data
        print("\nSample of transformed data:")
        print(transformed_df.head().to_string(index=False))
        
    except Exception as e:
        print(f"ETL Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
