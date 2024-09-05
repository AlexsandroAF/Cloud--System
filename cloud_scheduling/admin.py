from django.contrib import admin
from .models import Vehicles, \
    CompanyShippingTransport, \
    VehiclesListCompanyTransport, \
    AddressCompanyTransport, \
    VehiclesListCompanySupplier, \
    AddressCompanySupplier, \
    ContactCompanySupplier, \
    ContactCompanyTransport, \
    CompanySupplier, \
    Schedule, \
    ScheduleStatus, \
    NFe
from cloud_home.models import Company

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'date_create')


class CompanyShippingTransportAdmin(admin.ModelAdmin):
    list_display = ('corporate_name', 'registration_number', 'fantasy_name', 'service_kind', 'date_create')


class VehiclesListCompanyTransportAdmin(admin.ModelAdmin):
    list_display = ('id_vehicle', 'id_company_transport', 'description', 'date_create')


class AddressCompanyTransportAdmin(admin.ModelAdmin):
    list_display = ('district', 'number', 'city', 'reference', 'zip_code', 'id_company', 'date_create')


class VehiclesListCompanySupplierAdmin(admin.ModelAdmin):
    list_display = ('id_vehicle', 'id_company_supplier', 'description', 'date_create')


class AddressCompanySupplierAdmin(admin.ModelAdmin):
    list_display = ('district', 'number', 'city', 'reference', 'zip_code', 'id_company_supplier', 'date_create')


class ContactCompanySupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id_company', 'scheduling_number', 'representative_number', 'supplier_company_number', 'citizen_service_number',
        'email_adder')


class ContactCompanyTransportAdmin(admin.ModelAdmin):
    list_display = (
        'id_company', 'scheduling_number', 'representative_number', 'shipping_company_number', 'citizen_service_number',
        'email_adder')


class CompanySupplierAdmin(admin.ModelAdmin):
    list_display = (
        'shipping_type', 'corporate_name', 'fantasy_name', 'service_kind', 'need_schedule_collection',
        'registration_number',
        'state_registration', 'date_create')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'hour', 'date', 'id_main_company', 'id_company_supplier', 'id_company_transport', 'count_nfe', 'count_fullness',
        'status', 'date_create')


class NfeAdmin(admin.ModelAdmin):
    list_display = ('id_schedule', 'nfe_danfe', 'nfe_number', 'date_create')


class ScheduleStatusAdmin(admin.ModelAdmin):
    list_display = ('description', 'observation', 'date_create')


# Register your models here.
admin.site.register(Vehicles, VehiclesAdmin)
admin.site.register(CompanyShippingTransport, CompanyShippingTransportAdmin)
admin.site.register(VehiclesListCompanyTransport, VehiclesListCompanyTransportAdmin)
admin.site.register(AddressCompanyTransport, AddressCompanyTransportAdmin)
admin.site.register(VehiclesListCompanySupplier, VehiclesListCompanySupplierAdmin)
admin.site.register(AddressCompanySupplier, AddressCompanySupplierAdmin)
admin.site.register(ContactCompanySupplier, ContactCompanySupplierAdmin)
admin.site.register(ContactCompanyTransport, ContactCompanyTransportAdmin)
admin.site.register(CompanySupplier, CompanySupplierAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(ScheduleStatus, ScheduleStatusAdmin)
admin.site.register(NFe, NfeAdmin)
