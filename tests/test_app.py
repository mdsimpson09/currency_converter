import unittest
from app import app
from currency_converter import validate_currency_code, validate_amount, convert_currency

class CurrencyConverterTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Currency Converter</h1>', response.data)

    def test_invalid_currency_code(self):
        currency_code = 'XYZ'
        self.assertFalse(validate_currency_code(currency_code))

    def test_valid_currency_code(self):
        currency_code = 'USD'
        self.assertTrue(validate_currency_code(currency_code))

    def test_invalid_amount(self):
        amount = 'abc'
        self.assertFalse(validate_amount(amount))

    def test_valid_amount(self):
        amount = '100'
        self.assertTrue(validate_amount(amount))

    def test_convert_currency(self):
        from_currency = 'USD'
        to_currency = 'EUR'
        amount = 100
        result = convert_currency(from_currency, to_currency, amount)
        self.assertIsInstance(result, str)
        self.assertIn('€', result)

if __name__ == '__main__':
    unittest.main()