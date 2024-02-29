from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Booking(models.Model):
    STATUS_CONFIRM = 'C'
    STATUS_PENDING = 'P'
    STATUS_CANCELED = 'CA'
    STATUS_ATTENDED = 'A'
    STATUS_BOOK = [
        (STATUS_CONFIRM ,'CONFIRM'),
        (STATUS_ATTENDED , 'ATTENDED'),
        (STATUS_CANCELED , 'CANCELED'),
        (STATUS_PENDING , 'PENDING')
    ] 
    CASH_PAYMENT = 'P'
    CREDIT_CARD_PAYMENT = 'CC'
    PAYPAL_PAYMENT = 'PP'
    PAYMENT_METHOD = [
        (CASH_PAYMENT , 'CASH'),
        (CREDIT_CARD_PAYMENT, 'CREDIT CARD'),
        (PAYPAL_PAYMENT, 'PAYPAL')
    ]
    date_created = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=10, choices = STATUS_BOOK , default = STATUS_PENDING) 
    payment_method = models.CharField(max_length=10, choices= PAYMENT_METHOD , default = CASH_PAYMENT)
    note = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.status

class BookItem(models.Model):
    # what booking applied to what object 
    booking = models.ForeignKey(Booking, on_delete = models.CASCADE)
    # type (class , ..)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
