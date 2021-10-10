import calculator as c
import unittest
 
class TestGCD(unittest.TestCase):
 
    def test_GCD_trivial(self):
        result = c.gcd(1, 2)
        self.assertEqual(result, 1)

    def test_GCD_common(self):
        result = c.gcd(18, 12)
        self.assertEqual(result, 6)    

    def test_GCD_zero(self):
        self.assertRaises(ZeroDivisionError, c.gcd, 6, 0)

    def test_GCD_negative(self):
        result = c.gcd(1, -2)
        self.assertEqual(result, 1)  

    def test_gcd_neg_neg(self):
        result = c.gcd(-1, -2)
        self.assertEqual(result, 1)  
 
 
if __name__ == '__main__':
    unittest.main()
