import numbers
from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_city():
    assert extract_city()