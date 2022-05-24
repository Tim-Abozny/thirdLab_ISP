from django.test import TestCase


class URLTests(TestCase):
    def test_test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_test_feedback_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_test_register_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
