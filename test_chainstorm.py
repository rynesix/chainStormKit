# test_chainstorm.py
"""
Tests for chainStorm module.
"""

import unittest
from chainstorm import chainStorm

class TestchainStorm(unittest.TestCase):
    """Test cases for chainStorm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = chainStorm()
        self.assertIsInstance(instance, chainStorm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = chainStorm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
