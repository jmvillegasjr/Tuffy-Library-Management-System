from django.db import models


class Customer(models.Model):
    STATES = (
        ('CA', 'CA'),
        ('OR', 'OR'),
    )

    name = models.CharField(max_length=25, null=True)

    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=25, null=True)
    zip = models.IntegerField(null=True)
    state = models.CharField(max_length=2, null=True, choices=STATES)
    email = models.CharField(max_length=80, null=True)
    phone = models.CharField(max_length=14, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    book_title = models.CharField(max_length=255, null=True)
    isbn = models.IntegerField(null=True)
    date_received = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=25, null=True)
    publisher = models.CharField(max_length=25, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.book_title


class IssueOrder(models.Model):
    STATUS = (
        ('Checked Out', 'Checked Out'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_out = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)


class ReturnOrder(models.Model):
    STATUS = (
        ('Checked In', 'Checked In'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)



