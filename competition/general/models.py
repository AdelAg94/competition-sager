from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=265, unique=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True,null=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    photo = models.ImageField(upload_to='media/participants', null=True, blank=True)
    country = CountryField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.user.username