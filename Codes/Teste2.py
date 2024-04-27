# Jogo da velha em python
import unittest
from unittest.mock import patch
from io import StringIO
from flask import Flask

app = Flask(__name__)

class Palindromo:
    def is_palindrome(text):
    # Remova espaços e converta para letras minúsculas
        cleaned_text = text.replace(" ", "").lower()
        # Verifique se a string é igual à sua inversão
        return cleaned_text == cleaned_text[::-1]

class Test_Palindromo:
    # Testes unitários
    def test_is_palindrome(self):
        assert self.is_palindrome("radar")
        assert self.is_palindrome("level")
        assert self.is_palindrome("python")
        assert self.is_palindrome("subi no onibus")
        assert self.is_palindrome("socarram me subi no onibus em marrocos")

if __name__ == '__main__':
    unittest.main()