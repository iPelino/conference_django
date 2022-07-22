from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name