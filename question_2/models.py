from django.db import models

class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.latitude) + " , " + str(self.longitude)

class Operation(models.Model):

    '''
    max name length assumed to be 64
    '''
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Frequencies(models.Model):
    operation = models.ForeignKey(Operation, related_name="frequencies_operation", on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, related_name="frequencies_bin", on_delete=models.CASCADE)

    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['operation', 'bin'], name='Operaition-Bin pairs must be unique')
        ]

    def __str__(self):
        return self.operation.name + " - " + str(self.bin) + " - " + self.last_collection.strftime("%Y-%m-%d %H:%M") + " - " + str(self.collection_frequency)
