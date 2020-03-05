from django.db import models
# Create your models here.
class NewLeads(models.Model):
    title = models.CharField(max_length=100,default='title')
    source = models.CharField(max_length=100,default='source')
    description = models.CharField(max_length=100,default='desc')
    url = models.URLField(max_length=250)
    domain = models.FloatField()
    keyword=models.CharField(max_length=250)
    attachment = models.CharField(max_length=100,default='attachment')
    technology=models.CharField(max_length=250)
    est_budget=models.IntegerField()
    referredby = models.CharField(max_length=100)
    assignto = models.CharField(max_length=250)
    fullname  = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    company = models.CharField(max_length=250)
    registration = models.CharField(max_length=250)
    skypeId = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    country = models.CharField(max_length=150)
    phone = models.IntegerField()
    status=models.CharField(max_length=100,default="New")


    def __str__(self):
        return  self.title
