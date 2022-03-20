from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class BirthdayTest(TestCase):
    """Check if birthday logic is correct"""

    def setUp(self):
        url = reverse("birthday:index")
        self.client = Client()
        self.response = self.client.get(url)

    def test_correct_template_rendered(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'birth/index.html')
        self.assertTemplateNotUsed(self.response, 'birth/home.html')
        self.assertContains(self.response, 'Birthday')
    
    def test_birthday_logic(self):
        
        