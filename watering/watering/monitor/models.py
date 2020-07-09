from django.db import models

# Create your models here.

class monitor(models.Model):
    time = models.CharField(max_length=30,verbose_name="time")
    humidity = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="humidity")
    temperature = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="temperature")



class Monitor_2(models.Model):
    year = models.SmallIntegerField(verbose_name = "year")
    month = models.SmallIntegerField(verbose_name = "month")
    day = models.SmallIntegerField(verbose_name = "day")
    hour = models.SmallIntegerField(verbose_name = "hour")
    minute = models.SmallIntegerField(verbose_name = "minute")
    second = models.SmallIntegerField(verbose_name = "second")
    humidity = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="humidity")
    temperature = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="temperature")

class Monitor_3(models.Model):
    year = models.SmallIntegerField(verbose_name = "year")
    month = models.SmallIntegerField(verbose_name = "month")
    day = models.SmallIntegerField(verbose_name = "day")
    hour = models.SmallIntegerField(verbose_name = "hour")
    minute = models.SmallIntegerField(verbose_name = "minute")
    second = models.SmallIntegerField(verbose_name = "second")
    humidity = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="humidity")
    temperature = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="temperature")

