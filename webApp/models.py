from django.db import models

# Create your models here.

class resource(models.Model):
    desc = models.TextField()
    # img = models.ImageField(upload_to='pics')
    img = models.FileField(upload_to='pics')
    

