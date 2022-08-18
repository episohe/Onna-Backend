"""
Test for user models.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


def create_user(email='one@example.com', password='test1234', organization='onna'):
    return get_user_model().objects.create_user(email, password, organization)


class ModelTest(TestCase):
    """Test models."""

    def test_create_user(self):
        """Test creating a user successful"""
        email = 'two@example.com'
        password = 'test5678'
        name = '홍길동'
        phone = '010-1212-5656'
        organization = 'onna'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            organization=organization,
            name=name,
            phone=phone
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.organization, organization)
        self.assertEqual(user.name, name)
        self.assertEqual(user.phone, phone)
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        """Test email is normalized for user."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'email123', 'onna')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123', 'onna')

    def test_create_superuser(self):
        """Test creating superuser."""
        user = get_user_model().objects.create_superuser(
            'three@example.com',
            'test8902',
            'onna',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
