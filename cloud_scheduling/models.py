from datetime import datetime

from django.db import models
from django.utils import timezone

from cloud_home.models import Company


# Create your models here.
class Vehicles(models.Model):
    type = models.CharField(max_length=45, blank=False, verbose_name='Tipo de Veículo')
    description = models.TextField(max_length=150, blank=True, verbose_name='Descrição')
    date_create = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Data da Criação')

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name_plural = "Veículos"
        ordering = ['type']


# Modelos de Dados de Transporte
class CompanyShippingTransport(models.Model):
    registration_number = models.CharField(max_length=20, unique=True, verbose_name='CNPJ')
    corporate_name = models.CharField(max_length=150, blank=False, verbose_name='Razão Social')
    fantasy_name = models.CharField(max_length=150, blank=True, verbose_name='Nome Fantasia')
    state_registration = models.CharField(max_length=35, blank=True, verbose_name='Inscrição Estadual')
    service_kind = models.CharField(max_length=25, blank=True, verbose_name='Tipo de Serviço')
    value_shipping_int = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True,
                                             verbose_name='Valor do Frete')
    value_shipping_perc = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Valor do Frete %')
    date_create = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Data da Criação')

    def __str__(self):
        return str(self.corporate_name)

    class Meta:
        verbose_name_plural = "Transportadora"
        ordering = ['corporate_name']


class ContactCompanyTransport(models.Model):
    scheduling_number = models.CharField(max_length=25, verbose_name='Nrº Agendamento')
    representative_number = models.CharField(max_length=25, verbose_name='Nrº Representante')
    shipping_company_number = models.CharField(max_length=25, verbose_name='Nrº Transportadora')
    citizen_service_number = models.CharField(max_length=25, verbose_name='Nrº SAC')
    email_adder = models.CharField(max_length=80, verbose_name='E-mail')
    id_company = models.ForeignKey(CompanyShippingTransport, on_delete=models.CASCADE, verbose_name='Transportadora')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.id_company) + ' - ' + str(self.email_adder)

    class Meta:
        verbose_name_plural = "Contatos Transportadoras"
        ordering = ['date_create']


class AddressCompanyTransport(models.Model):
    district = models.CharField(max_length=75, verbose_name='Bairro')
    number = models.CharField(max_length=75, verbose_name='Número')
    city = models.CharField(max_length=75, verbose_name='Cidade')
    reference = models.CharField(max_length=75, verbose_name='Referencia')
    zip_code = models.CharField(max_length=75, verbose_name='CEP')
    latitude = models.CharField(max_length=75, verbose_name='Latitude')
    longitude = models.CharField(max_length=75, verbose_name='Longitude')
    id_company = models.ForeignKey(CompanyShippingTransport, on_delete=models.CASCADE, verbose_name='Transportadora')
    date_create = models.DateTimeField(auto_now_add=True, editable=False, )

    def __str__(self):
        return str(self.id_company), str(self.zip_code)

    class Meta:
        verbose_name_plural = "Endereços Transportadora"
        ordering = ['date_create']


# Tipos de veicules necessário
class VehiclesListCompanyTransport(models.Model):
    id_vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, verbose_name='Veiculo')
    id_company_transport = models.ForeignKey(CompanyShippingTransport, on_delete=models.CASCADE,
                                             verbose_name='Transportadora')
    description = models.TextField(max_length=150, blank=True, verbose_name='Descrição')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.id_vehicle)

    class Meta:
        verbose_name_plural = "Lista de Veículos Transportado"
        ordering = ['date_create']


# Modelos de Dados de Fornecedor
class CompanySupplier(models.Model):
    shipping_type = models.CharField(max_length=5, blank=False, verbose_name='CIF ou FOB')
    registration_number = models.CharField(max_length=20, unique=True, verbose_name='CNPJ')
    corporate_name = models.CharField(max_length=150, blank=False, verbose_name='Razão Social')
    fantasy_name = models.CharField(max_length=150, blank=True, verbose_name='Nome Fantasia')
    state_registration = models.CharField(max_length=35, blank=True, verbose_name='Inscrição Estadual')
    service_kind = models.CharField(max_length=25, blank=True, verbose_name='Tipo de Serviço')
    need_schedule_collection = models.BooleanField(blank=False, verbose_name='Necessário Agendamento Coleta')
    vehicle_list = models.ManyToManyField(Vehicles)
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.corporate_name)

    class Meta:
        verbose_name_plural = "Fornecedor"
        ordering = ['date_create']


class ContactCompanySupplier(models.Model):
    scheduling_number = models.CharField(max_length=25, blank=True, verbose_name='Nrº Agendamento')
    representative_number = models.CharField(max_length=25, blank=True, verbose_name='Nrº Representante')
    supplier_company_number = models.CharField(max_length=25, blank=True, verbose_name='Nrº Fornecedor')
    citizen_service_number = models.CharField(max_length=25, blank=True, verbose_name='Nrº SAC')
    email_adder = models.CharField(max_length=80, verbose_name='E-mail')
    id_company = models.ForeignKey(CompanySupplier, on_delete=models.CASCADE, verbose_name='Fornecedor')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.email_adder)

    class Meta:
        verbose_name_plural = "Contatos Fornecedor"
        ordering = ['date_create']


class AddressCompanySupplier(models.Model):
    district = models.CharField(max_length=75, verbose_name='Bairro')
    number = models.CharField(max_length=75, verbose_name='Número')
    city = models.CharField(max_length=75, verbose_name='Cidade')
    reference = models.CharField(max_length=75, verbose_name='Referencia')
    zip_code = models.CharField(max_length=75, verbose_name='CEP')
    latitude = models.CharField(max_length=75, verbose_name='Latitude')
    longitude = models.CharField(max_length=75, verbose_name='Longitude')
    id_company_supplier = models.ForeignKey(CompanySupplier, on_delete=models.CASCADE, verbose_name='Fornecedor')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.zip_code)

    class Meta:
        verbose_name_plural = "Endereços Fornecedor"
        ordering = ['date_create']


# Tipos de veicules necessário
class VehiclesListCompanySupplier(models.Model):
    id_vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, verbose_name='Veículo')
    id_company_supplier = models.ForeignKey(CompanySupplier, on_delete=models.CASCADE, verbose_name='Fornecedor')
    description = models.TextField(max_length=150, blank=True, verbose_name='Descrição')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.id_vehicle)

    class Meta:
        verbose_name_plural = "Lista de Veículos Fornecedor"
        ordering = ['id_company_supplier']


# Tabelas de Agendamento
class ScheduleStatus(models.Model):
    description = models.CharField(max_length=45, blank=False, unique=True, verbose_name="Descrição")
    observation = models.CharField(max_length=90, blank=True, verbose_name="Observação")
    date_create = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return str(self.description)

    class Meta:
        verbose_name_plural = "Status do Agendamento"
        ordering = ['date_create']


class Schedule(models.Model):
    id_main_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa Agendada')
    id_company_supplier = models.ForeignKey(CompanySupplier, on_delete=models.CASCADE, verbose_name='Fornecedor')
    id_company_transport = models.ForeignKey(CompanyShippingTransport, on_delete=models.CASCADE,
                                             verbose_name='Transportadora')
    hour = models.TimeField(blank=False, verbose_name='Hora da Entrega')
    date = models.DateField(blank=False, verbose_name='Data da Entrega')
    status = models.ForeignKey(ScheduleStatus, blank=False, on_delete=models.CASCADE, verbose_name="Status")
    count_nfe = models.IntegerField(blank=True, verbose_name='Quantidade de Notas')
    count_fullness = models.IntegerField(blank=True, verbose_name='Quantidade de Volumes')
    date_create = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(id)

    class Meta:
        verbose_name_plural = "Agenda de Entregas"
        ordering = ['date', 'hour']

    def is_delayed_time(self):
        # Lógica para verificar se o agendamento está atrasado em relação ao horário
        return self.hour < datetime.now().time()

    def is_delayed_days(self):
        # Lógica para verificar se o agendamento está atrasado em relação aos dias
        return self.date < datetime.now().date()

    def is_cancelled(self):
        # Lógica para verificar se o agendamento está cancelado
        return self.status == 'cancelado'

    def is_delivered(self):
        # Lógica para verificar se o agendamento está entregue
        return self.status == 'entregue'

    def is_suspended(self):
        # Lógica para verificar se o agendamento está suspenso
        return self.status == 'suspenso'


class NFe(models.Model):
    id_schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name="ID Agendamento")
    nfe_danfe = models.CharField(max_length=75, blank=False, unique=True, verbose_name='DANFE')
    nfe_number = models.CharField(max_length=75, blank=False, verbose_name='Numero da NFe')
    date_create = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Data de Criação')

    def __str__(self):
        return str(self.nfe_number)

    class Meta:
        verbose_name_plural = "Lista de Notas Fiscais"
        ordering = ['id_schedule', 'date_create']
