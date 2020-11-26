from django.db import models

# Create your models here.

class Resources(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    img = models.ImageField(upload_to = 'stats/images/')
    url  = models.URLField(blank = True)


    def __str__(self):
        return self.title


class News(models.Model):
    title= models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    img = models.ImageField(upload_to = 'stats/images/')
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title