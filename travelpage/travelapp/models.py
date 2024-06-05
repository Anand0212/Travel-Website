from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.



class EventFull(models.Model):
    CAT = ((1, 'Day Trek'), (2, 'Camping'), (3, 'Family Tour'), (4, 'Backpacking'))
    LOC = ((1, 'Maharashtra'), (2, 'Sikkim'), (3, 'Uttarakhand'), (4, 'Karnataka'), (5, 'Himachal Pradesh'))
    e_name = models.CharField(max_length=50)
    e_category = models.IntegerField(choices=CAT, verbose_name='category')
    e_desc = models.CharField(max_length=300)
    e_date = models.DateField()
    e_image = models.ImageField(upload_to='images', default='1')
    e_price = models.FloatField(default=0)
    e_state = models.IntegerField(choices=LOC, verbose_name='state')
    e_itinerary = models.TextField(default='abc')

    def __str__(self) -> str:
        return self.e_name
    

class Enroll(models.Model):
    c_name = models.CharField(max_length=30)
    c_mobile = models.BigIntegerField()
    no_participants = models.IntegerField()


class Confirm(models.Model):
    userid = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_column='u_id')
    eid = models.ForeignKey('EventFull', on_delete=models.CASCADE, db_column='e_id')
    # n_participants = models.IntegerField(default=1)
    participants = models.IntegerField(default=1)

class Enqiury(models.Model):
    name = models.CharField(max_length=40)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)    
    emial = models.EmailField(unique=True, null=False, blank=False)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)