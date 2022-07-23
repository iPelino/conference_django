from django.db import models


class Speaker(models.Model):

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='F')

    class Meta:
        verbose_name = "speaker"
        verbose_name_plural = "Speakers"

    def __str__(self):
        return self.name


class Conference(models.Model):
    title = models.CharField(max_length=200)
    speakers = models.ManyToManyField(Speaker)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2) #100000.00

    def __str__(self):
        return self.title


class Schedule(models.Model):
    topic = models.CharField(max_length=100)
    speaker = models.ForeignKey(Speaker, on_delete=models.PROTECT)
    start_time = models.TimeField()
    end_time = models.TimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return self.conference.title + " - " + self.topic
