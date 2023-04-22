from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

User = get_user_model()


class Account(models.Model):
    class Gender(models.TextChoices):
        MALE = "Masculino"
        FEMALE = "Femenino"

    id = models.CharField(
        max_length=36,  default=uuid4, primary_key=True, editable=False, verbose_name="ID", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=45, verbose_name="First Name")
    last_name = models.CharField(max_length=45, verbose_name="Last Name")

    phone = models.CharField(max_length=9, verbose_name="Phone Number")
    dob = models.DateField(verbose_name="Date of Birth")
    dni = models.CharField(max_length=8, unique=True, verbose_name="DNI")

    gender = models.CharField(
        max_length=100,
        choices=Gender.choices,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['dni'], name='unique_dni')
        ]
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
