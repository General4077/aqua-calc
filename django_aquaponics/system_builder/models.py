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


class SystemType(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class System(models.Model):

    name = models.CharField(max_length=200)
    system_type = models.ForeignKey(SystemType, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name

    def bsa(self):
        return sum([f.bsa for f in self.filters])


class Filter(models.Model):

    media = models.ForeignKey(Media, on_delete=models.DO_NOTHING)
    volume = models.FloatField()
    system = models.ForeignKey(System, on_delete=models.CASCADE)

    @property
    def bsa(self):
        return self.media.ssa * self.volume

    def __str__(self):
        return f'{self.media.name}: {self.volume} ft\u0033'




class Fish(models.Model):

    name = models.CharField(max_length=200)
