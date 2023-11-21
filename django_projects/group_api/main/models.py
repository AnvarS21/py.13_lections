from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    psevdonim = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return  self.psevdonim if self.psevdonim \
            else f'{self.first_name} {self.last_name}'

class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Musician, on_delete=models.CASCADE, related_name='songs')
    feat = models.ForeignKey(
        Musician, on_delete=models.CASCADE, related_name='feats',
        blank=True,
        null=True)
    poster = models.ImageField(upload_to='images',
                               blank=True,
                               null=True)
    date = models.DateField()

    def __str__(self):
        if self.feat:
            return  f'{self.author} - {self.title} ft. {self.feat}'
        return  f'{self.author} - {self.title}'

class Grammy(models.Model):
    owner = models.OneToOneField(Musician, on_delete=models.CASCADE)
    year = models.DateField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return  f'{self.owner} - Grammy {self.year}'
