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
        if self.pk is None:
            User.objects.create_user(email=self.email, password=self.password, username=self.username,
                                     first_name=self.first_name, last_name=self.last_name)
        else:
            User.objects.update(email=self.email, password=self.password, username=self.username,
                                first_name=self.first_name, last_name=self.last_name)
        super(Customer, self).save(force_insert, force_update, using, update_fields)
        try:
            Cart.objects.get(belongs_to=self)
        except Cart.DoesNotExist:
            Cart.objects.create(belongs_to=self)

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


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.name, self.category.name)

    @property
    def get_price(self):
        return int(self.price)

    @property
    def get_quanitity(self):
        return int(self.quantity)


class Cart(models.Model):
    belongs_to = models.OneToOneField(Customer, on_delete=models.CASCADE, unique=True, null=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Cart of {}'.format(self.belongs_to.full_name())

    def items(self):
        return len(self.item.objects)
