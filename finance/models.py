from django.db import models

# Create your models here.

class MyStocks(models.Model):
    #id = models.AutoField(primary_key=True)
    Buy_Date = models.DateField()
    Sell_Date = models.DateField(null=True, blank=True)
    Symbol = models.CharField(max_length=6, default="x")
    Quanity = models.IntegerField(default=0)
    Buy_Price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    Sell_Price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    def __str__(self):
        return "{} {} {} {} {}".format(self.Buy_Date, self.Sell_Date, self.Symbol, self.Quanity, self.Buy_Price, self.Sell_Price)

class Prices(models.Model):
    #id = models.AutoField(primary_key=True)
    Date = models.DateField()
    Symbol = models.CharField(max_length=6, default="x")
    Price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    def __str__(self):
        return "{} {} {}".format(self.Date, self.Symbol, self.Price)
