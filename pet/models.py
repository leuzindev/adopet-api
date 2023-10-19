from django.db import models


class Shelter(models.Model):
    name = models.CharField(
        max_length=255
    )
    located_at = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Pet(models.Model):
    SMALL = 1
    MEDIUM = 2
    BIG = 3
    PET_SIZES = (
        (SMALL, 'Porte pequeno'),
        (MEDIUM, 'Porte médio'),
        (BIG, 'Porte Grande'),
    )
    name = models.CharField(
        max_length=100
    )
    avatar = models.ImageField(
        upload_to="pet_pics/",
        blank=True,
        null=True,
    )
    age = models.IntegerField()
    build = models.PositiveSmallIntegerField(
        'Role',
        choices=PET_SIZES,
    )
    short_description = models.CharField(
        max_length=155,
        blank=True,
        null=True,
    )
    located_at = models.CharField(
        max_length=255
    )
    shelter = models.ForeignKey(
        Shelter,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
