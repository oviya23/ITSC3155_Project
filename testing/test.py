import unittest
import requests

class FlaskTest(unittest.TestCase):

    def test_home(self):
        response = requests.get("http://127.0.0.1:5000/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<h1>Welcome to the ROCS Q&A App!</h1>' in response.text, True)

    def test_questions(self):
        response = requests.get("http://127.0.0.1:5000/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('Title' and 'Date' in response.text, True)

    def test_question(self):
        response = requests.get("http://127.0.0.1:5000/home/1")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('First Question' in response.text, True)

    def test_new(self):
        response = requests.get("http://127.0.0.1:5000/home/new")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual('<form action="new" method="post">' in response.text, True)

    def test_delete(self):
        response = requests.get('http://127.0.0.1:5000/home/delete/<question_id>')
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)

if __name__ == " __main__":
    unittest.main()
