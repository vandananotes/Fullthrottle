from django.db import models
from datetime import datetime

class ActivityPeriod(models.Model):
    activity_periods_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.activity_periods_id)

class User(models.Model):
    id  = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=100, default=None)
    tz = models.CharField(max_length=100, default=None)
    activity_periods = models.ForeignKey(
        ActivityPeriod, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return str(self.id)


