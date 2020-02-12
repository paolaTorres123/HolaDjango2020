from django.test import TestCase

# Create your tests here.
class TestSmoke(TestCase):
    def test_smoke_Test(self):
        self.assertEqual(2+2,4)
    def test_smoke_Test(self):
        self.assertEqual(2+3,5)
