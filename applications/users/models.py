from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid

from applications.users.functions import validar_rut

from applications.regioncomuna.models import Comuna, Region

from .managers import UserManager


class University(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de la Universidad")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región")
    TYPE_CHOICES = (
        ('publica', 'Pública'),
        ('privada', 'Privada')
    )
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, verbose_name="Tipo")

    def __str__(self):
        return self.name


class Profession(models.Model):
    PROFESSION = (
        ('Arquitecto', 'Arquitecto'),
        ('Ingeniero Civil en Obras Civiles', 'Ingeniero Civil en Obras Civiles'),
        ('Ingeniero Eléctrico', 'Ingeniero Eléctrico'),
        ('Ingeniero Hidráulico', 'Ingeniero Hidráulico'),
        ('Constructor Civil', 'Constructor Civil'),
        ('Topógrafo', 'Topógrafo'),
        ('Otros', 'Otros'),
    )

    profession = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class User(AbstractBaseUser, PermissionsMixin):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256, blank=True)
    rut = models.CharField(max_length=15, validators=[validar_rut], unique=True, blank=True, null=True)
    score = models.IntegerField(default=0)
    profession = models.ManyToManyField(Profession, verbose_name='Profesiones', blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_number = models.CharField(max_length=20, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(unique=True, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='company_owner', on_delete=models.CASCADE)
    partner = models.ManyToManyField(User, related_name='company_partner', blank=True)
    rut = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_number = models.CharField(max_length=20, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)


class Score(models.Model):
    score = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="El puntaje debe ser entre 1 mínimo y 5 como máximo.")
    comment = models.CharField(max_length=255)
    user_owner = models.ForeignKey(User, related_name='score_owner', on_delete=models.CASCADE)
    user_writer = models.ForeignKey(User, related_name='score_writer', on_delete=models.CASCADE)


class Patent(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    user_owner = models.ForeignKey(User, related_name='patent_owner', on_delete=models.CASCADE)
    number = models.IntegerField()
    category = models.CharField(max_length=100)
    validity_date = models.DateField(blank=True, null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    document = models.FileField(upload_to='patents/', blank=True, null=True)


class Role(models.Model):
    ROLE = (
        ('Propietario/a',  'Propietario/a'),
        ('Arquitecto', 'Arquitecto'),
        ('Constructor', 'Constructor'),
        ('Revisor independiente',  'Revisor independiente'),
        ('Calculista',  'Calculista'),
        ('Revisor de Cálculo', 'Revisor de Cálculo'),
        ('Coordinador', 'Coordinador')
    )
    role = models.CharField(max_length=100, choices=ROLE)
