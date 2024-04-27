import unittest

class Palindromo:

    def is_palindrome(text):
        # Remova espaços e converta para letras minúsculas
        cleaned_text = text.replace(" ", "").lower()
        # Verifique se a string é igual à sua inversão
        return cleaned_text == cleaned_text[::-1]

class Test_Palindromo(unittest.TestCase):
    # Testes unitários
    def test_is_palindrome(self):
        assert Palindromo.is_palindrome("radar")
        assert Palindromo.is_palindrome("level")
        assert Palindromo.is_palindrome("osso")
        assert Palindromo.is_palindrome("subi no onibus")
        assert Palindromo.is_palindrome("ana")

if __name__ == '__main__':
    unittest.main()
