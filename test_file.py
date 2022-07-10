import pytest
from Contract import Contract

def test_a():
  c = Contract()
  assert("aaa", c.get_symbol())
  assert True
  
