#!/usr/bin/env python3

import pytest
import pandas as pd
import json
import os
import tempfile
import shutil
from datetime import datetime
import sys

# Add the parent directory to the path to import etl module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl import extract, transform, load_csv, load_json


class TestETLPipeline:
    """Test suite for ETL pipeline functions"""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing"""
        return pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['john doe', 'jane smith', 'bob johnson'],
            'age': [28, 34, 45],
            'city': ['New York', 'Los Angeles', 'Chicago'],
            'salary': [75000, 82000, 68000]
        })
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing"""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    def test_extract(self):
        """Test the extract function"""
        # Test with actual data file
        df = extract()
        
        # Assertions
        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert list(df.columns) == ['id', 'name', 'age', 'city', 'salary']
        assert len(df) == 10  # Should have 10 records from input.csv
    
    def test_transform(self, sample_data):
        """Test the transform function"""
        # Transform the sample data
        transformed_df = transform(sample_data)
        
        # Assertions
        assert isinstance(transformed_df, pd.DataFrame)
        assert len(transformed_df) == len(sample_data)
        
        # Check new columns exist
        expected_columns = ['id', 'name', 'age', 'age_group', 'city', 'salary', 'salary_category', 'processed_at']
        assert list(transformed_df.columns) == expected_columns
        
        # Check salary categories
        assert 'salary_category' in transformed_df.columns
        assert set(transformed_df['salary_category'].unique()).issubset({'High', 'Medium', 'Low'})
        
        # Check age groups
        assert 'age_group' in transformed_df.columns
        assert set(transformed_df['age_group'].unique()).issubset({'Senior', 'Mid', 'Junior'})
        
        # Check name formatting (title case)
        assert all(name == name.title() for name in transformed_df['name'])
        
        # Check processed_at is a valid timestamp
        assert 'processed_at' in transformed_df.columns
        assert all(isinstance(pd.to_datetime(row), datetime) for row in transformed_df['processed_at'])
    
    def test_salary_categorization(self, sample_data):
        """Test salary categorization logic"""
        transformed_df = transform(sample_data)
        
        # Check specific salary categorizations
        high_salary = transformed_df[transformed_df['salary'] >= 80000]
        medium_salary = transformed_df[(transformed_df['salary'] >= 60000) & (transformed_df['salary'] < 80000)]
        low_salary = transformed_df[transformed_df['salary'] < 60000]
        
        assert all(high_salary['salary_category'] == 'High')
        assert all(medium_salary['salary_category'] == 'Medium')
        assert all(low_salary['salary_category'] == 'Low')
    
    def test_age_grouping(self, sample_data):
        """Test age grouping logic"""
        transformed_df = transform(sample_data)
        
        # Check specific age groupings
        senior = transformed_df[transformed_df['age'] >= 40]
        mid = transformed_df[(transformed_df['age'] >= 30) & (transformed_df['age'] < 40)]
        junior = transformed_df[transformed_df['age'] < 30]
        
        assert all(senior['age_group'] == 'Senior')
        assert all(mid['age_group'] == 'Mid')
        assert all(junior['age_group'] == 'Junior')
    
    def test_load_csv(self, sample_data, temp_dir):
        """Test CSV loading function"""
        # Change to temp directory
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Load data to CSV
            load_csv(sample_data)
            
            # Check if file was created
            assert os.path.exists('output/transformed_data.csv')
            
            # Check file contents
            loaded_df = pd.read_csv('output/transformed_data.csv')
            assert len(loaded_df) == len(sample_data)
            assert list(loaded_df.columns) == list(sample_data.columns)
            
        finally:
            os.chdir(original_cwd)
    
    def test_load_json(self, sample_data, temp_dir):
        """Test JSON loading function"""
        # Change to temp directory
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Load data to JSON
            load_json(sample_data)
            
            # Check if file was created
            assert os.path.exists('output/transformed_data.json')
            
            # Check file contents
            with open('output/transformed_data.json', 'r') as f:
                json_data = json.load(f)
            
            assert 'metadata' in json_data
            assert 'data' in json_data
            assert json_data['metadata']['total_records'] == len(sample_data)
            assert len(json_data['data']) == len(sample_data)
            assert 'processed_at' in json_data['metadata']
            assert 'columns' in json_data['metadata']
            
        finally:
            os.chdir(original_cwd)
    
    def test_data_integrity(self, sample_data):
        """Test that data integrity is maintained through transformation"""
        transformed_df = transform(sample_data)
        
        # Check that original data is preserved
        assert len(transformed_df) == len(sample_data)
        assert all(transformed_df['id'] == sample_data['id'])
        assert all(transformed_df['age'] == sample_data['age'])
        assert all(transformed_df['salary'] == sample_data['salary'])
        assert all(transformed_df['city'] == sample_data['city'])
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Test with empty DataFrame
        empty_df = pd.DataFrame(columns=['id', 'name', 'age', 'city', 'salary'])
        transformed_empty = transform(empty_df)
        assert len(transformed_empty) == 0
        assert list(transformed_empty.columns) == ['id', 'name', 'age', 'age_group', 'city', 'salary', 'salary_category', 'processed_at']
    
    def test_full_pipeline_integration(self):
        """Test the full ETL pipeline integration"""
        # This test runs the actual pipeline with real data
        # Note: This will use the actual data/input.csv file
        
        # Extract
        df = extract()
        assert len(df) > 0
        
        # Transform
        transformed_df = transform(df)
        assert len(transformed_df) == len(df)
        assert 'salary_category' in transformed_df.columns
        assert 'age_group' in transformed_df.columns
        
        # Load (these will create files in the current directory)
        load_csv(transformed_df)
        load_json(transformed_df)
        
        # Verify files were created
        assert os.path.exists('output/transformed_data.csv')
        assert os.path.exists('output/transformed_data.json')
        
        # Verify CSV content
        csv_df = pd.read_csv('output/transformed_data.csv')
        assert len(csv_df) == len(transformed_df)
        
        # Verify JSON content
        with open('output/transformed_data.json', 'r') as f:
            json_data = json.load(f)
        assert json_data['metadata']['total_records'] == len(transformed_df)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
