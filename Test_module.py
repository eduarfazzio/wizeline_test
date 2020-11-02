import unittest
import Test_Api
import os


class TestCases(unittest.TestCase):
    def setUp(self):
        Test_Api.app.testing = True
        self.app = Test_Api.app.test_client()

    def test_hello(self):
        result = self.app.get('/hello')
        self.assertEqual(result.data, b'Hello Wolrd!')

    def test_covid_all(self):
        result = self.app.get('/covid_data/all')
        self.assertNotEqual(result.data, b'Country not found')

    def test_covid_mx(self):
        result = self.app.get('/covid_data/mx')
        self.assertNotEqual(result.data, b'Country not found')

    def test_covid_error(self):
        result = self.app.get('/covid_data/m')
        self.assertEqual(result.data, b'Country not found')

    def test_covid_notFound(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'no_reponse.txt')
        with open(my_file, 'r') as file:
            data_txt_file = file.read()
        result = self.app.get('/otherLink')
        self.assertNotEqual(result.data, data_txt_file)

if __name__ == "__main__":
    unittest.main()