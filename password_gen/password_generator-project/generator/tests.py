from django.test import TestCase
from generator.views import generate_pwd
import string

# Create your tests here.
class PasswordGeneratorTest(TestCase):

    def test_len(self):
        pwd = generate_pwd(5, lower=True)
        self.assertEqual(5, len(pwd))

    def test_len_2(self):
        pwd = generate_pwd(18, lower=True, upper=True, specials=True, numbers=True)
        self.assertEqual(18, len(pwd))

    def test_only_lower(self):
        for _ in range(1000):
            pwd = generate_pwd(10, lower=True)
            self.assertTrue(pwd.islower())

    def test_only_upper(self):
        for _ in range(1000):
            pwd = generate_pwd(10, upper=True)
            self.assertTrue(pwd.isupper())
