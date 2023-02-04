from django.db import models
from management.models import Volunteer
# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(unique=True)
    severity = models.IntegerField(
        choices=[
            (1, 'Level 1'),
            (2, 'Level 2'),
            (3, 'Level 3')
        ]
    )
    created = models.DateTimeField(auto_created=True) 
    assignee = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, blank=True, null=True)
    location_lat = models.FloatField()
    location_lon = models.FloatField()

    class Meta:
        unique_together = ('name','description',)
        
    def __str__(self):
        return self.name


    

