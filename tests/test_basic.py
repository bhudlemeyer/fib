import unittest
import requests

class BasicTests(unittest.TestCase):
    def test_base_function(self):
        response = requests.get('http://localhost:8080/')
        self.assertEqual(200, response.status_code, response.status_code)


    def test_fib_endpoint(self):
        response = requests.get("http://localhost:8080/v1/fib/5")
        self.assertEqual(200, response.status_code, response.status_code)

    def test_fib_negative_num_response(self):
        response = requests.get("http://localhost:8080/v1/fib/-1")
        self.assertEqual(404, response.status_code, response.status_code)

    def test_fib_word_response(self):
        response = requests.get("http://localhost:8080/v1/fib/hello")
        self.assertEqual(404, response.status_code, response.status_code)

    def test_fib_incorrect_endpoint(self):
        response = requests.get("http://localhost:8080/fib")
        self.assertEqual(404, response.status_code, response.status_code)


if __name__ == "__main__":
    unittest.main()
