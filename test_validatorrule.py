# test_validatorrule.py
"""
Tests for ValidatorRule module.
"""

import unittest
from validatorrule import ValidatorRule

class TestValidatorRule(unittest.TestCase):
    """Test cases for ValidatorRule class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ValidatorRule()
        self.assertIsInstance(instance, ValidatorRule)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ValidatorRule()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
