from django.forms import ModelForm, Select, TimeInput, DateInput
from cloud_home.models import Company
from django.views.generic import ListView
from .models import *


class MainCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['registration_number',
                  'corporate_name',
                  'fantasy_name',
                  'fantasy_name',
                  'description']


class VehiclesListForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = ['type',
                  'description']


class CompanyShippingListForm(ModelForm):
    class Meta:
        model = CompanyShippingTransport
        fields = ['registration_number',
                  'corporate_name',
                  'fantasy_name',
                  'state_registration',
                  'service_kind',
                  'value_shipping_int',
                  'value_shipping_perc']


class CompanySupplierForm(ModelForm):
    class Meta:
        model = CompanySupplier
        fields = ['shipping_type',
                  'registration_number',
                  'corporate_name',
                  'fantasy_name',
                  'state_registration',
                  'service_kind',
                  'need_schedule_collection']


class ListNfeForm(ModelForm):
    class Meta:
        model = NFe
        fields = [
            'id_schedule',
            'nfe_danfe',
            'nfe_number'
        ]


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'id_main_company',
            'id_company_supplier',
            'id_company_transport',
            'hour',
            'date',
            'status',
            'count_nfe',
            'count_fullness'
        ]
        widgets = {
            'hour': TimeInput(format='%H:%M'),
            'date': DateInput()
        }


class ContactCompanySupplierForm(ModelForm):
    class Meta:
        model = ContactCompanySupplier
        fields = [
            'scheduling_number',
            'representative_number',
            'supplier_company_number',
            'citizen_service_number',
            'email_adder',
            'id_company',
        ]


class AddressCompanySupplierForm(ModelForm):
    class Meta:
        model = AddressCompanySupplier
        fields = [
            'district',
            'number',
            'city',
            'reference',
            'zip_code',
            'latitude',
            'longitude',
            'id_company_supplier',
        ]


class ContactCompanyShippingForm(ModelForm):
    class Meta:
        model = ContactCompanyTransport
        fields = [
            'scheduling_number',
            'representative_number',
            'shipping_company_number',
            'citizen_service_number',
            'email_adder',
            'id_company',
        ]


class AddressCompanyShippingForm(ModelForm):
    class Meta:
        model = AddressCompanyTransport
        fields = [
            'district',
            'number',
            'city',
            'reference',
            'zip_code',
            'latitude',
            'longitude',
            'id_company',
        ]
