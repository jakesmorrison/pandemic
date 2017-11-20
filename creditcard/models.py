from django.db import models

# Create your models here.

class CreditStatus(models.Model):
    status = models.CharField(max_length=50, default='-')
    holder = models.CharField(max_length=50, default='-')
    issuer = models.CharField(max_length=50, default='-')
    card = models.CharField(max_length=50, default='-')
    issuedate = models.DateField()
    closedate = models.DateField()
    line = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    minspend = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {}".format(self.status,self.holder,self.issuer,self.card,self.issuedate,
                                                      self.closedate,self.line,self.fee,self.minspend,self.bonus)

class PointsUsed(models.Model):
    date = models.DateField()
    where = models.CharField(max_length=50, default='-')
    what = models.CharField(max_length=50, default='-')
    dollar_cost = models.IntegerField(default=0)
    point_cost = models.IntegerField(default=0)
    info = models.CharField(max_length=50, default='-')
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.date,self.where,self.what,self.dollar_cost,self.point_cost,self.info)

