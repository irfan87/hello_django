from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    def test_homepage_exists_at_correct_location(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
