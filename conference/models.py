from django.contrib.auth.models import User
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
    con_theme = models.TextField(max_length=500, null=True, blank=True)
    speakers = models.ManyToManyField(Speaker)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2) #100000.00
    description = models.TextField(null=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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


class Participant(models.Model):
    ROLE_CHOICES = (
        ('BED', 'Back End Developer'),
        ('FED', 'Front End Developer'),
        ('FSD', 'Full Stack Developer'),
        ('DES', 'Designer'),
        ('STU', 'Student'),
        ('ENT', 'Enthusiast'),
        ('OTH', 'Other'),
    )
    name = models.CharField(max_length=200)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    motivation = models.TextField(null=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


''' CREATING MODEL OBJECTS'''

# ModelName.objects.create()
# create an instance of the Model --> obj  = ModelName() --> obj.save()
