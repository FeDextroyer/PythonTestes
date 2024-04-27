from flask import Flask, request, jsonify

app = Flask(__name__)

class Primo:
    
   def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

import unittest
class Test_Primo(unittest.TestCase):
    def test_is_prime(self):
        assert self.is_prime(2)
        assert self.is_prime(3)
        assert self.is_prime(5)
        assert self.is_prime(7)
        assert self.is_prime(10)

if __name__ == '__main__':
    app.run(debug=True)