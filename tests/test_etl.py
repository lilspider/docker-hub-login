import pytest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from etl import extract, transform

def test_extract():
    df = extract()
    assert len(df) > 0
    assert 'id' in df.columns

def test_transform():
    df = pd.DataFrame({
        'id': [1, 2],
        'name': ['john doe', 'jane smith'],
        'age': [25, 35],
        'city': ['New York', 'Los Angeles'],
        'salary': [50000, 80000]
    })
    result = transform(df)
    assert 'salary_category' in result.columns
    assert 'age_group' in result.columns
