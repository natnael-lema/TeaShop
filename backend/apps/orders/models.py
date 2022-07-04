from django import db
from django.db import models
from apps.items.models import Item
from apps.users.models import User
from config.constants import *
# Create your models here.


class Order(models.Model):
    class Meta(object):
        db_table = 'order'
    
    user = models.ForeignKey(
        User,on_delete=models.CASCADE,default='Aninymnous'
    )
    total_price = models.DecimalField(
        'Total Price',blank=False,null= False, max_digits=14,decimal_places=2
    )
    full_name = models.CharField(
        'Full Name',blank=False,null = False,max_length=20,db_index=True,default='Aninymnous'
    )
    address_line1 = models.CharField(
        'Address Line 1',blank=False,null = False,max_length=60,db_index=True,default='Aninymnous'
    )
    address_line2 = models.CharField(
        'Address Line 2',blank=False,null = False,max_length=60,db_index=True,default='Aninymnous'
    )
    city = models.CharField(
        'City',blank=False,null = False,max_length=20,db_index=True
    )
    state = models.CharField(
        'State',blank=False,null = False,max_length=20,db_index=True
    )
    postal_code = models.IntegerField(
        'Postal Code', blank=False, db_index=True
    )
    country = models.CharField(
        'Country',blank=False,null = False,max_length=20,db_index=True
    )
    telephone = models.IntegerField(
        'Telephone', blank=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )


class OrderItem(models.Model):
    class Meta(object):
        db_table = 'order item'

    order = models.IntegerField(
        'Order Id', blank=False, db_index=True
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(
        'Quantity', blank=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )



