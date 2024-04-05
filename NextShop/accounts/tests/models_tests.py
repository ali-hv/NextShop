from django.contrib.auth import get_user_model
from django.test import TestCase

from .factories import UserFactory


class UserModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = UserFactory()

    def test_user_creation(self):
        # Test user creation
        self.assertTrue(isinstance(self.user, get_user_model()))

    def test_string_representation(self):
        # Test string representation
        self.assertEqual(str(self.user), self.user.username)

    def test_create_superuser(self):
        # Create a test superuser using factory
        superuser = UserFactory(is_staff=True, is_superuser=True)

        # Test superuser creation
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
