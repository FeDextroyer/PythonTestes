import unittest

class Primo:
    
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

class Test_Primo(unittest.TestCase):
    def test_is_prime(self):  # Adicione 'self' como argumento
        self.assertTrue(Primo.is_prime(2))
        self.assertTrue(Primo.is_prime(3))
        self.assertTrue(Primo.is_prime(5))
        self.assertTrue(Primo.is_prime(7))
        self.assertFalse(Primo.is_prime(10))  # 10 não é primo

if __name__ == '__main__':
    unittest.main()
