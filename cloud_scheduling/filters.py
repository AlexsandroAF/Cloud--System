import django_filters
from .models import Schedule

from .models import CompanySupplier
from .models import CompanyShippingTransport
from .models import ScheduleStatus


class ScheduleFilter(django_filters.FilterSet):
    idMainCompany = django_filters.CharFilter(field_name='idMainCompany__corporateName', lookup_expr='icontains',
                                              label='Empresa')
    idCompanySupplier = django_filters.CharFilter(field_name='idCompanySupplier__corporateName',
                                                  lookup_expr='icontains', label='Fornecedor')
    idCompanyTransport = django_filters.CharFilter(field_name='idCompanyTransport__corporateName',
                                                   lookup_expr='icontains', label='Transportadora')

    start_hour = django_filters.TimeFilter(field_name='hour', lookup_expr='gte', label="Hora Inicial")
    end_hour = django_filters.TimeFilter(field_name='hour', lookup_expr='lte', label="Hora Final")

    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte', label='Data Inicial')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte', label='Data Final')

    thisStatus = django_filters.ModelChoiceFilter(field_name='status', queryset=ScheduleStatus.objects.filter(),
                                                  label='Status')

    class Meta:
        model = Schedule
        fields = ['id_main_company',
                  'id_company_supplier',
                  'id_company_transport',
                  'hour',
                  'date',
                  'status']


class CompanySupplierFilter(django_filters.FilterSet):
    shippingType = django_filters.CharFilter(lookup_expr='icontains', label='Tipo')
    registrationNumber = django_filters.CharFilter(lookup_expr='icontains', label='CNPJ')
    fantasyName = django_filters.CharFilter(lookup_expr='icontains', label='Nome Fantasia')
    serviceKind = django_filters.CharFilter(lookup_expr='icontains', label='Tipo de Serviço')
    needSchedulesCollection = django_filters.BooleanFilter(field_name='needSchedulesCollection', label='Faz Coleta?')

    class Meta:
        model = CompanySupplier
        fields = [
            'shipping_type',
            'registration_number',
            'fantasy_name',
            'service_kind',
            'need_schedule_collection',
        ]


class CompanyShippingTransportFilter(django_filters.FilterSet):
    fantasyName = django_filters.CharFilter(lookup_expr='icontains', label='Nome Fantasia')
    stateRegistration = django_filters.CharFilter(lookup_expr='icontains', label='CNPJ')
    serviceKind = django_filters.CharFilter(lookup_expr='icontains', label='Tipo')
    valueShippingInt = django_filters.CharFilter(lookup_expr='icontains', label='Valor Frete Inteiro')
    valueShippingPerc = django_filters.CharFilter(lookup_expr='icontains', label='Valor Frete Porcentagem (%)')

    class Meta:
        model = CompanyShippingTransport
        fields = [
            'fantasy_name',
            'service_kind',
            'value_shipping_int',
            'value_shipping_perc',
        ]
