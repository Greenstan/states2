from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    abbreviation = models.CharField(max_length= 2, null=True, blank=True)
    
    def __unicode__(self):
        return '%s' % self.name

class StateCapital(models.Model):
    state = models.OneToOneField("app.State", null=True)
    name = models.CharField( max_length=300, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True,blank=True)
    population = models.IntegerField(null=True, blank=True)

    def __unicode__ (self):
        return '%s' % self.name 

class City(models.Model):
    state = models.ForeignKey( "app.State", null=True)
    name = models.CharField( max_length=300, null=True, blank=True)
    longitude = models.FloatField( null=True, blank=True)
    latitude = models.FloatField( null=True,blank=True)
    zipcode = models.IntegerField(null=True,blank=True)
    county = models.CharField(max_length=300,null=True,blank=True)

    def __unicode__ (self):
        return '%s' % self.name



