from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6 ,
                                 decimal_places = 2,
                                 validators = [MinValueValidator(1)])
    avaliable_time = models.TimeField()
    
    def __str__(self) -> str:
        return self.name
    

class Coach(models.Model):
    MORNING_PERIOD = 'M'
    EVENING_PERIOD = 'E'
    AFTERNOON_PERIOD = 'A'
    STATUS_TIME = [
        (MORNING_PERIOD ,'morining'),
        (EVENING_PERIOD , 'evening'),
        (AFTERNOON_PERIOD , 'afternoon')
    ] 
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    bio = models.TextField()
    suitable_period = models.CharField(max_length=1, choices = STATUS_TIME , default = MORNING_PERIOD) 

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    class Meta:
        ordering = ['first_name' , 'last_name']

class Trainee(models.Model):
    MEMBER_BODY_BUILDING = 'B'
    MEMBER_EARN_WEIGHT = 'E'
    MEMBER_LOSE_WEIGHT = 'L'
    MEMBER_FITNESS = 'F'
    MEMBER_CHOICES = [
        (MEMBER_BODY_BUILDING , 'body building'),
        (MEMBER_EARN_WEIGHT , 'earn weight'),
        (MEMBER_LOSE_WEIGHT , 'lose weight'),
        (MEMBER_FITNESS , 'fitness')
    ]
    MORNING_PERIOD = 'M'
    EVENING_PERIOD = 'E'
    AFTERNOON_PERIOD = 'A'
    STATUS_TIME = [
        (MORNING_PERIOD ,'moring'),
        (EVENING_PERIOD , 'evening'),
        (AFTERNOON_PERIOD , 'afternoon')
    ] 
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    phone = PhoneNumberField(blank = True)
    birth_date = models.DateField(null =True)
    ultimate_goal = models.CharField(max_length=1, choices = MEMBER_CHOICES , default =MEMBER_LOSE_WEIGHT)
    suitable_period = models.CharField(max_length=1, choices = STATUS_TIME , default = MORNING_PERIOD) 
    sport = models.ForeignKey(Sport , on_delete = models.PROTECT,related_name='trainee')
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        ordering = ['first_name', 'last_name']
        

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    zip = models.IntegerField()
    trainee = models.ForeignKey(Trainee, on_delete = models.PROTECT)

class Class(models.Model):
    BEGINNER  = 'B'
    INTERMEDIATE = 'I'
    ADVANCE = 'A'
    LEVEL = [
        (BEGINNER ,'beginner'),
        (INTERMEDIATE , 'intermediate'),
        (ADVANCE , 'advance')
    ] 
    MORNING_PERIOD = 'M'
    EVENING_PERIOD = 'E'
    AFTERNOON_PERIOD = 'A'
    STATUS_TIME = [
        (MORNING_PERIOD ,'moring'),
        (EVENING_PERIOD , 'evening'),
        (AFTERNOON_PERIOD , 'afternoon')
    ] 
    class_name = models.CharField(max_length =255, default = 'class_a')
    description = models.TextField()
    capacity = models.IntegerField()
    image = models.ImageField(blank=True)
    start_time = models.TimeField(null = True)
    date = models.DateField(auto_now = True)
    duration = models.IntegerField()
    level = models.CharField(max_length=1, choices = LEVEL , default =INTERMEDIATE)
    suitable_period = models.CharField(max_length=1, choices = STATUS_TIME , default = MORNING_PERIOD) 
    sport = models.ForeignKey(Sport , on_delete = models.PROTECT)
    coach = models.ForeignKey(Coach , on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.class_name
    
    class Meta:
        ordering = ['class_name']

class ClassItem(models.Model):
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
    # number_of_trainee = models.IntegerField()
    trainee = models.ForeignKey(Trainee , on_delete = models.CASCADE)
    payment = models.IntegerField()
    status = models.CharField(max_length=10, choices = STATUS_BOOK , default = STATUS_PENDING) 
    classes = models.ForeignKey(Class , on_delete = models.CASCADE)  

class Review(models.Model):
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE, related_name = 'review')
    name = models.CharField(max_length= 255)
    description = models.TextField()
    star = models.IntegerField()
    date = models.DateField(auto_now_add=True)




