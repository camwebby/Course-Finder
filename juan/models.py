from django.db import models

#class coursetest(models.Model):
#    institution = models.CharField(max_length=50)
#    name = models.CharField(max_length=50)
#    typeC = models.CharField(max_length=10)
#    salary = models.IntegerField(null=True)
#    tariff = models.FloatField(default=0.0)

class course1(models.Model):
    institution = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    label = models.CharField(max_length=15)
    url = models.CharField(max_length=150)
    mode = models.CharField(max_length=15)
    salary = models.IntegerField(null=True)
    avgTariff = models.FloatField(null=True)
    minTariff = models.FloatField(null=True)
    employment = models.FloatField(null=True)
