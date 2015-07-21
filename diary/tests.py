from django.test import TestCase

# Create your tests here.

from .models import Customer
from django.contrib.auth.models import User

class CustomerTests(TestCase):
    
    def test_anonymous_customer_exists(self):
        """
        Check that there is an anonymous customer and user for use by the diary 
        app.
        """
#        anonymousCustomer = Customer.objects.get(pk=1)
#        anonymousUser = anonymousCustomer.user
#        self.assertEqual(anonymousUser.username, 'anon')
        anonymousCustomer = Customer.objects.get(pk=1)
        self.assertEqual(anonymousCustomer.username, 'anon')
