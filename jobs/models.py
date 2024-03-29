from django.db import models

# Create your models here.
class Job(models.Model):
    # Images
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 100, default = 'Some String')
    # summary
    summary = models.CharField(max_length = 300)

    def __str__(self):
        return self.title
