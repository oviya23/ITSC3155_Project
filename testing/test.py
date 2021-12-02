import unittest
import requests

class FlaskTest(unittest.TestCase):

    def test_loginHTML(self):
        response = requests.get("http://127.0.0.1:5000/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<h1>Welcome to the ROCS Q&A App!</h1>' in response.text, True)

    def test_login(self):
        response = requests.get("http://127.0.0.1:5000/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<form method="POST" action="/login">' in response.text, True)

    def test_registerHTML(self):
        response = requests.get("http://127.0.0.1:5000/register")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<h1>Welcome to the ROCS Q&A App!</h1>' in response.text, True)

    def test_register(self):
        response = requests.get("http://127.0.0.1:5000/register")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<form method="POST" action="/register">' in response.text, True)

if __name__ == " __main__":
    unittest.main()
