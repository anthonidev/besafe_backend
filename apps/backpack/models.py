from apps.home.models import HomeGroup
from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from cloudinary.models import CloudinaryField

User = get_user_model()


class Element(models.Model):

    class Type(models.TextChoices):
        FOOD = "food"
        HEALTH = "health"

    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True)
    name = models.CharField(max_length=45, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    icon = CloudinaryField('icon', overwrite=True,
                           format="webp", blank=True, null=True)

    type = models.CharField(
        max_length=100,
        choices=Type.choices,
        verbose_name="Type"
    )

    def __str__(self):
        return f"{self.name} - {self.type}"

    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"
        ordering = ['type']


class ElementItem(models.Model):
    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True)
    element = models.ForeignKey(
        Element, on_delete=models.CASCADE,
        related_name='groups'
    )

    date_added = models.DateField(verbose_name="Date Added", auto_now=True)
    count = models.IntegerField(verbose_name="Count")
    date_expiration = models.DateField(
        verbose_name="Date Expiration",
        null=True,
        blank=True
    )
    last_update = models.DateField(verbose_name="Last Update", auto_now=True)

    class Meta:
        verbose_name = "Elemento Item"
        verbose_name_plural = "Elementos Items"
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.element.name} - {self.count}"


class Food(models.Model):
    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True)
    last_update = models.DateField(verbose_name="Last Update", auto_now=True)
    elements = models.ManyToManyField(ElementItem)
    home_group = models.ForeignKey(
        HomeGroup, on_delete=models.CASCADE, related_name='food')

    class Meta:
        app_label = 'Víveres'
        verbose_name = "Víveres"
        verbose_name_plural = "Víveres"


class Health(models.Model):
    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True)
    last_update = models.DateField(verbose_name="Last Update", auto_now=True)
    elements = models.ManyToManyField(ElementItem)
    home_group = models.ForeignKey(
        HomeGroup, on_delete=models.CASCADE, related_name='health')

    class Meta:
        app_label = 'Botiquín'
        verbose_name = "Botiquín"
        verbose_name_plural = "Botiquines"
