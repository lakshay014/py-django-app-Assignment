from django.db import models

# Create your models here.
class Events(models.Model):
    sno = models.IntegerField(db_column='SNO', primary_key=True)  # Field name made lowercase.
    event_name = models.CharField(max_length=50, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    image = models.CharField(max_length=2000, blank=True, null=True)
    is_liked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'events'
