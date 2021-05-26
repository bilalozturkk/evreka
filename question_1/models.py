import datetime

from django.db import models

class Vehicle(models.Model):

    '''
    max plate length assumed to be 10
    '''
    plate = models.CharField(max_length=10)

    def __str__(self):
        return self.plate

    def has_recent_navigation_record(self, query_time):
        return True if self.navigationrecords.filter(datetime__gte=query_time - datetime.timedelta(days=2)).count() > 0 else False

    def most_recent_navigation_record(self, query_time):
        return self.navigationrecords.filter(datetime__gte=query_time - datetime.timedelta(days=2)).order_by('-datetime').first()

class NavigationRecord(models.Model):

    '''
    on_delete strategy chosen to be CASCADE,
    if a vehicle is deleted then the navigation records
    related to the vehicle will also be deleted
    '''
    vehicle = models.ForeignKey(Vehicle, related_name='navigationrecords', on_delete=models.CASCADE)

    '''
    there is no detail present about the specifications
    of these fields suchs as float field details etc. That's why
    these details have not been taken care of.
    '''

    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.vehicle.plate + " - " + self.datetime.strftime("%Y-%m-%d %H:%M")