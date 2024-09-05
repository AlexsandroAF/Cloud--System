from django.db import models
from django.utils import timezone


# Create your models here.
class Company(models.Model):
    registration_number = models.CharField(max_length=25, blank=False)
    corporate_name = models.CharField(max_length=45, blank=True)
    fantasy_name = models.CharField(max_length=45, blank=True)
    status = models.BooleanField(default=True, verbose_name='Empresa Ativa')
    description = models.CharField(max_length=125)

    def __str__(self):
        return self.corporate_name

    class Meta:
        verbose_name_plural = "Empresa"
        ordering = ['status']

class Departament(models.Model):
    description = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.description


class Group(models.Model):
    description = models.CharField(max_length=125, unique=True)
    departament = models.ForeignKey(Departament, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.description


class Account(models.Model):
    account_name = models.CharField(max_length=45)
    account_last_name = models.CharField(max_length=45)
    account_email = models.CharField(max_length=150)
    account_password = models.CharField(max_length=255)
    account_dtcreate = models.DateTimeField(default=timezone.now)
    account_dtedit = models.DateTimeField(default=timezone.now)
    account_depart = models.ForeignKey(Departament, on_delete=models.DO_NOTHING)
    account_group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    account_last_ip = models.CharField(max_length=30, blank=True)
    account_last_session_name = models.CharField(max_length=30, blank=True)
    account_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    account_disable = models.BooleanField(default=False)

    def __str__(self):
        return self.account_name


class HotfixLog(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Título')
    details = models.TextField(blank=False, verbose_name='Descrição')
    version = models.CharField(max_length=20, blank=False, verbose_name='Versão')
    date_create = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Lista de Atualização"


class SuggestionLog(models.Model):
    username = models.CharField(max_length=45, blank=True, verbose_name='Usuario')
    suggestion = models.TextField(blank=False, verbose_name='Sugestão')
    date_create = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Lista de Sugestão"