import unittest

class Par_Impar:
   
   def is_odd(number):
    return number % 2 != 0

class Test_Par_Impar(unittest.TestCase):
    def test_is_odd(self):
        self.assertFalse(Par_Impar.is_odd(2))
        self.assertTrue(Par_Impar.is_odd(3))
        self.assertTrue(Par_Impar.is_odd(5))
        self.assertTrue(Par_Impar.is_odd(7))
        self.assertFalse(Par_Impar.is_odd(10))

if __name__ == "__main__":
    unittest.main()
    