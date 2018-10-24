from django.db import models


g=(('male','MALE'),
   ('female','FEMALE'))

ag=(('pee-wee','PEE-WEE'),
    ('sub junior','SUB JUNIOR'),
    ('junior','JUNIOR'),
    ('senior','SENIOR'),
    ('senior black belt','SENIOR BLACK BELT'))

wg=(('fin','FIN'),
    ('fly','FLY'),
    ('bantam','BANTAM'),
    ('feather','FEATHER'),
    ('light','LIGHT'),
    ('welter','WELTER'),
    ('light Middle','LIGHT MIDDLE'),
    ('middle','MIDDLE'),
    ('light Heavy','LIGHT HEAVY'),
    ('heavy','HEAVY'))

g1=(('male','MALE'),
   ('female','FEMALE'))

ag1=(('pee-wee','PEE-WEE'),
    ('sub junior','SUB JUNIOR'),
    ('junior','JUNIOR'),
    ('senior','SENIOR'),
    ('senior black belt','SENIOR BLACK BELT'))

wg1=(('fin','FIN'),
    ('fly','FLY'),
    ('bantam','BANTAM'),
    ('feather','FEATHER'),
    ('light','LIGHT'),
    ('welter','WELTER'),
    ('light Middle','LIGHT MIDDLE'),
    ('middle','MIDDLE'),
    ('light Heavy','LIGHT HEAVY'),
    ('heavy','HEAVY'))

class Players(models.Model):
    user=models.CharField(max_length=50)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=6,choices=g,default='male')
    age=models.CharField(max_length=4)
    agegroup=models.CharField(max_length=20,choices=ag,default='senior')
    weight=models.CharField(max_length=200)
    weightcategory=models.CharField(max_length=12,choices=wg,default='fin')
    PlayingFor=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)

class Results(models.Model):
    user = models.CharField(max_length=50)
    agegroup = models.CharField(max_length=20, choices=ag1, default='senior')
    gender = models.CharField(max_length=6, choices=g1, default='male')
    weightcategory = models.CharField(max_length=12, choices=wg1, default='fin')
    gold=models.CharField(max_length=50,default='Null')
    silver=models.CharField(max_length=50,default='Null')
    bronze1=models.CharField(max_length=50,default='Null')
    bronze2=models.CharField(max_length=50,default='Null')

