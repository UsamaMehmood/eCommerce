from django.test import TestCase
from django.urls import reverse

class TestHomeView(TestCase):
    def test_home_view(self):
        result = self.client.get(reverse('store:home'))
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, 'store/home.html')
