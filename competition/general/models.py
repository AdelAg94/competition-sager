from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
# Create your models here.

# This to make email unqiue for users 
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

class Skill(models.Model):
    name = models.CharField(max_length=265, unique=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length=265, default='Web Developer')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    photo = models.ImageField(upload_to='media/participants', null=True, blank=True)
    country = CountryField()
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.user.username

class Competition(models.Model):
    name = models.CharField(max_length=265, unique=True)
    description = models.CharField(max_length=1500, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    photo = models.ImageField(upload_to='media/competitions', null=True, blank=True)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    description = models.CharField(max_length=265)
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE, blank=True, null=True, related_name='qualifications')

    def __str__(self):
        return str(self.competition) + " - "  +  self.description[0:10] 