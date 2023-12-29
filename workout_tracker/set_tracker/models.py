from django.db import models

# Create your models here.
class SetTracker(models.Model):
    day = models.CharField(max_length=80, blank=False, default='')
    sets = models.IntegerField(blank=True, default=3)
    comments = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='set_tracker', on_delete=models.CASCADE)

    class Meta:
        ordering = ['day'] # If '-day' is given the order will be desending.
