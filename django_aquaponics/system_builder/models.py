from django.db import models

class Crop(models.Model):

    name = models.CharField(max_length=200)
    root_area = models.FloatField()


    def __str__(self):
        return f'Root Area: {self.root_area} ft\u00B2/ft\u00B2'




class Media(models.Model):

    name = models.CharField(max_length=200)
    ssa = models.FloatField()

    def __str__(self):
        return f'{self.name}: SSA = {self.ssa} ft\u00B2/ft\u00B3'


class Filter(models.Model):

    media = models.ForeignKey(Media, on_delete=models.DO_NOTHING)
    volume = models.FloatField()


    @property
    def bsa(self):
        return self.media.ssa * self.volume


class Fish(models.Model):

    name = models.CharField(max_length=200)