from django.urls import path
from . import views
from .filters import ScheduleFilter, CompanySupplierFilter, CompanyShippingTransportFilter
from .views import nfe_delete, ScheduleUpdateView

urlpatterns = [
    # Urls Agenda
    path('agendamento/agenda/', views.SchedulesListView.as_view(filterset_class=ScheduleFilter),
         name='schedulesDisplay'),
    path('agendamento/agendados/add', views.SchedulesNewView.as_view(), name='schedules_add'),
    path('agendamento/agendados/update/<int:pk>', views.ScheduleUpdateView.as_view(), name='scheduleUpdate'),
    path('agendamento/nfe/delete/<int:nfe_id>/', ScheduleUpdateView.as_view(), name='schedule_nfe_delete'),
    path('agendamento/delete/<int:schedule_id>/', views.schedule_delete, name='schedule_delete'),

    # Urls Fornecedores
    path('agendamento/fornecedores/', views.CompanySupplierListView.as_view(filterset_class=CompanySupplierFilter),
         name='companySupplierListDisplay'),
    path('agendamento/fornecedores/add', views.CompanySupplierNew.as_view(), name='company_supplier_add'),
    path('agendamento/fornecedores/delete/<int:company_supplier_id>', views.company_supplier_delete,
         name='company_supplier_delete'),
    path('agendamento/fornecedores/update/<int:pk>', views.CompanySupplierUpdateView.as_view(),
         name='companySupplierUpdate'),

    # Urls Transportadoras
    path('agendamento/transportadoras/', views.CompanyShippingListView.as_view(
        filterset_class=CompanyShippingTransportFilter),
         name='companyShippingListDisplay'),
    path('agendamento/transportadoras/add', views.CompanyShippingNew.as_view(), name='company_shipping_new'),
    path('agendamento/transportadoras/delete/<int:company_shipping_id>', views.company_shipping_delete,
         name='company_shipping_delete'),
    path('agendamento/transportadoras/update/<int:pk>', views.CompanyShippingUpdateView.as_view(),
         name='companyShippingUpdate'),

    path('lista_empresas/', views.company_list_display, name='companyListDisplay'),
    path('lista_veiculos/', views.vehicles_list_display, name='vehiclesListDisplay'),
    path('lista_nfe/', views.nfe_list_display, name='nfeListDisplay'),

]
