from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, UserManager

import datetime

# Create your models here.

phoneValidator = RegexValidator(
    regex=r'[0-9][0-9 ]+',
    message='Not a valid phone number')


class CustomerManager(UserManager):

    def get_by_natural_key(self, username):
        """
        Enable serialisation without pk. Not needed ATM.
        """
        return self.get(username=username)

    def create_user(self, 
        username, 
        first_name, 
        last_name, 
        email, 
        phone, 
        date_of_birth, 
        password=None
    ):
        """
        Creates and saves a Customer with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Customers must have a username')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Customer(User):
    """ Customer/Client/Patient details. 
    """
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    objects = CustomerManager()

    phone = models.CharField(
        max_length=20, 
        validators=[phoneValidator], 
        blank=True, 
        null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def natural_key(self):
        """
        Serialisation aid. Not needed ATM.
        """
        return (self.first_name,)

    def age(self):
        now = timezone.now()
        return now.year - self.date_of_birth.year

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

