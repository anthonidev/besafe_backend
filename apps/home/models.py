from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from cloudinary.models import CloudinaryField

from apps.identify.models import Account

User = get_user_model()


class HomeGroup(models.Model):

    class Material(models.TextChoices):
        ESTERA = "Estera"
        CONCRETO = "Concreto"
        MADERA = "Madera"

    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True
    )
    name = models.CharField(max_length=45, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")

    build_year = models.CharField(max_length=4, verbose_name="Build Year")
    build_material = models.CharField(
        max_length=100,
        choices=Material.choices,
    )
    family_code = models.CharField(
        max_length=8,
        unique=True,
        verbose_name="Family ID",
        blank=True,
        null=True
    )

    members = models.ManyToManyField(
        Account,
    )

    class Meta:
        verbose_name = "Hogar"
        verbose_name_plural = "Hogares"

    def save(self, *args, **kwargs):
        if not self.family_code:
            code = str(uuid4())[:8]
            while HomeGroup.objects.filter(family_code=code).exists():
                code = str(uuid4())[:8]
            self.family_code = code
        super().save(*args, **kwargs)


class Floor(models.Model):
    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True)
    number = models.IntegerField(verbose_name="Number")
    safe_zone = models.CharField(max_length=255, verbose_name="Safe Zone")
    picture = CloudinaryField('picture', overwrite=True,
                              format="webp", blank=True, null=True)
    home_group = models.ForeignKey(
        HomeGroup, on_delete=models.CASCADE, related_name='floors')

    class Meta:
        verbose_name = "Piso"
        verbose_name_plural = "Pisos"
        ordering = ['number']

    def __str__(self):
        return f"{self.home_group.name} piso: {self.number}"
