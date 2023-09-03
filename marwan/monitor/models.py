from django.db import models

# Create your models here.

class Symbol(models.Model):
    symbol = models.CharField(max_length=200,unique=True)
    lastPrice = models.FloatField()
    priceChangePercent = models.FloatField()
    highPrice = models.FloatField()
    lowPrice = models.FloatField()
    quoteVolume = models.FloatField()
    inGreen = models.IntegerField(default=0)

    def __str__(self):
        return self.symbol