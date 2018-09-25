from django.db import models

# Create your models here.
YEAR=(("FE","FE"),("SE","SE"),("TE","TE"),("BE","BE"),)

class classes(models.Model):
    year = models.CharField(choices=YEAR,max_length=10);
    division = models.PositiveSmallIntegerField(default=1);
    
    def __str__(self):
        return "{} {}".format(self.year,self.division)
    