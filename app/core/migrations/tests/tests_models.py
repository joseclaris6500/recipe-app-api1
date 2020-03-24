#Test that model can create a user
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        #TEst creating a new user with an email is successful
        email = "joseclaris65@yahoo.com"
        password = "Joseis44"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normaized(self):
        email = "joseclaris65@YAHOO.COM"
        user = get_user_model().objects.create_user(email, "test1234")
        self.assertEqual(user.email, email.lower())

    def test_create_new_superuser(self):
        "TEst creating a new superuser"
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)