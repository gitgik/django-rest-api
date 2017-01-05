from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.bucketlist), self.name)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.bucketlist = Bucketlist(name=self.name)

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        response = self.client.post(reverse('create'), self.bucketlist_data)
        self.assertEqual(response.status_code, 201)
