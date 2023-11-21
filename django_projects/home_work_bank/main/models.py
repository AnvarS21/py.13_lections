from django.db import models
from .constants import TypeChoices
from datetime import date
# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Human(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.DateField()
    telephone_number = models.IntegerField()
    gender = models.CharField(max_length=10)
    passport_id = models.IntegerField(unique=True)
    human_image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_year} {self.telephone_number} {self.gender} {self.passport_id}'


class Card(models.Model):
    card_number = models.PositiveBigIntegerField(unique=True)
    type = models.CharField(choices=TypeChoices.choices, default=TypeChoices.VISA, max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    owner = models.ForeignKey(Human, on_delete=models.CASCADE)
    # period = models.DateField(default=date.year+10)
    def __str__(self):
        return f'{self.type} {self.bank}'




