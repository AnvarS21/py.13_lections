from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'