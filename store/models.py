from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=25, default='')
    last_name = models.CharField(max_length=25, default='')
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=25, help_text='This will be used for your authentication, i-e Login')
    password = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        User.objects.create_user(email=self.email, password=self.password, username=self.username,
                                 first_name=self.first_name, last_name=self.last_name)
        return super(Customer, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        if not self.first_name == '' and not self.last_name == '':
            return '{} {}'.format(self.first_name, self.last_name)
        return '{} {}'.format(self.username, self.email)

    def full_name(self):
        if self.first_name == '' and self.last_name == '':
            return ''
        elif self.last_name == '':
            return self.first_name
        elif self.first_name == '':
            return self.last_name

        return '{} {}'.format(self.first_name, self.last_name)
