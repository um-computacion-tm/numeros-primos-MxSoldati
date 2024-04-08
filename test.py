import unittest
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertTrue(result)
    
    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)
    
    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)
    
    def test_with_6(self):
        result = is_prime(6)
        self.assertFalse(result)
    
    def test_with_13(self):
        result = is_prime(13)
        self.assertTrue(result)
    
    def test_with_101(self):
        result = is_prime(101)
        self.assertTrue(result)
    
    def test_with_997(self):
        result = is_prime(997)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()