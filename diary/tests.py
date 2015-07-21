import datetime
from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import Customer
from django.contrib.auth.models import User


def yearsago(years, from_date=None):
    """
    Workaround for datetime.timedelta not knowing how to calculate leap years.
    Adapted from:
    http://stackoverflow.com/questions/765797/python-timedelta-in-years
    """
    if from_date is None:
        from_date = timezone.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29 # can be removed
        return from_date.replace(month=2, day=28,
                                 year=from_date.year-years)


class CustomerTests(TestCase):

    def test_anonymous_customer_exists(self):
        """
        Check that there is an anonymous customer for use by the diary app.
        """
        anonymousCustomer = Customer.objects.get(username='anon')
        self.assertIsNotNone(anonymousCustomer)

    def test_customer_age(self):
        """
        Make sure the customer age calculation works correctly and as expected.
        """
        tenYearsAgo = yearsago(10)
        tenYearCustomer = Customer.objects.create(
            username='Ten',
            password='random',
            date_of_birth=tenYearsAgo,
        )
        self.assertEqual(tenYearCustomer.age(), 10)

    def test_customer_age_date_of_birth_not_set(self):
        """
        Make sure something sensible happens when we calculate age from an 
        undefined birth date.
        """
        undefinedBirthCustomer = Customer.objects.create(
            username='Ageless',
            password='random',
        )
        self.assertIsNone(undefinedBirthCustomer.age())

