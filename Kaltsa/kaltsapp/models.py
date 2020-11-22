from django.db import models
from django.contrib.auth.models import User
# TODO:  Add the imageField to the database

# Create your models here.
class State(models.Model):
    state = models.CharField(max_length=50, null=True)

    def __str__(self):
        stateName = '{0.state}'

        return stateName.format(self)

class Municipio(models.Model):
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        municipioName = '{0.name}'

        return municipioName.format(self)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        info = 'Name: {0.user.first_name}'
        return info.format(self)

class MissingPerson(models.Model):
    TYPE_I = "Piel muy clara o blanca"
    TYPE_II = "Piel clara"
    TYPE_III = "Piel clara intermedia"
    TYPE_IV = "Piel morena o media"
    TYPE_V = "Piel oscura o marrón"
    TYPE_VI = "Piel muy oscura o negra"

    SKIN_COLOR_CHOICES = [
        (TYPE_I, "Piel muy clara o blanca"),
        (TYPE_II, "Piel clara"),
        (TYPE_III, "Piel clara intermedia"),
        (TYPE_IV, "Piel morena o media"),
        (TYPE_V, "Piel oscura o marrón"),
        (TYPE_VI, "Piel muy oscura o negra"),
    ]

    MALE = "Masculino"
    FEMALE = "Female"

    GENDER_CHOICES = [
        (MALE, "Masculino"),
        (FEMALE, "Female"),
    ]
    # General Information
    full_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default = "Género", null=True)

    # Person's physical characteristics
    height = models.FloatField(null=True)
    hair_color = models.CharField(max_length=200, null=True)
    skin_color = models.CharField(max_length=100, choices=SKIN_COLOR_CHOICES, default="Color de piel")

    eye_color = models.CharField(max_length=50, null=True)
    unique_characteristics = models.CharField(max_length=300, null=True)

    person_image = models.ImageField(default="default.png", null=True, blank=True)

    # Persons last known location
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)

    last_seen_in = models.CharField(max_length=300, null=True)
    date_and_time = models.DateTimeField(auto_now_add=False, null=True)
    additional_info = models.CharField(max_length=200)

    def __str__(self):
        info = 'Name: {0.full_name}'
        # , Age: {0.age}'
        return info.format(self)


class Clue(models.Model):
    # Seen in
    clue_of = models.ForeignKey(MissingPerson, null=True, on_delete=models.CASCADE)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)

    seen_in = models.CharField(max_length=300)
    date_and_time = models.DateTimeField(auto_now_add=False, null=True)

    additional_info = models.CharField(max_length=200)

    # Contact number of person who gave the clue
    phone_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        clue = '{0.seen_in}'
        return clue.format(self)
