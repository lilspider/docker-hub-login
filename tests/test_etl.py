import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl import extract, transform

def test_extract():
    df = extract()
    assert len(df) > 0

def test_transform():
    df = extract()
    result = transform(df)
    assert 'salary_category' in result.columns
