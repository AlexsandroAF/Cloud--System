from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django_filters.views import FilterView
from django.views.generic.edit import FormView, UpdateView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Vehicles, \
    CompanyShippingTransport, \
    CompanySupplier, \
    Schedule, \
    NFe, ContactCompanySupplier, AddressCompanySupplier

from cloud_home.models import Company

from .forms import \
    CompanyShippingListForm, \
    CompanySupplierForm, \
    VehiclesListForm, \
    ScheduleForm, ListNfeForm, ContactCompanySupplierForm, AddressCompanySupplierForm, \
    ContactCompanyShippingForm, AddressCompanyShippingForm

from .filters import ScheduleFilter, CompanySupplierFilter, CompanyShippingTransportFilter


@login_required
def company_list_display(request):
    main_company = Company.objects.all()
    return render(request, 'cloud_scheduling/companyListDisplay.html', {
        'mainsCompany': main_company
    })


@login_required
def vehicles_list_display(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'cloud_scheduling/vehiclesListDisplay.html', {
        'vehicles': vehicles
    })


@login_required
def company_shipping_list_display(request):
    company_shipping_list = CompanyShippingTransport.objects.all()
    return render(request, 'cloud_scheduling/companyShippingListDisplay.html', {
        'companyShippingList': company_shipping_list
    })


# Views da Lista de NFe
@login_required
def nfe_list_display(request):
    nfe_list = NFe.objects.all()
    return render(request, 'cloud_scheduling/nfeListDisplay.html', {
        'formNfeList': nfe_list
    })


# Views da Lista de Agendamentos
@method_decorator(login_required, name='dispatch')
class SchedulesListView(PermissionRequiredMixin, FilterView):
    permission_required = 'app.can_view_schedule'
    model = Schedule
    filterset_class = ScheduleFilter
    paginate_by = 20
    template_name = 'cloud_scheduling/schedulesListDisplay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = self.get_queryset()
        paginator = Paginator(schedule, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            schedule_paginator = paginator.page(page)
        except PageNotAnInteger:
            schedule_paginator = paginator.page(1)
        except EmptyPage:
            schedule_paginator = paginator.page(paginator.num_pages)

        context['schedules'] = schedule_paginator
        context['form'] = ScheduleForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form_a = ScheduleForm(request.POST)

            if form_a.is_valid():
                form_a.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form_a.errors})
        else:
            return super().post(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class SchedulesNewView(PermissionRequiredMixin, FormView):
    permission_required = 'app.can_view_schedule'
    form_class = ScheduleForm
    template_name = 'cloud_scheduling/schedulesListDisplay.html'
    success_url = 'schedules_add'

    def form_valid(self, form):
        schedule_form = form.save(commit=False)
        schedule_form.hour = form.cleaned_data['hour']
        schedule_form.date = form.cleaned_data['date']

        if form.is_valid():  # Verifica a validade do formulário
            schedule_form.save()
            return redirect('schedulesDisplay')

        return super().form_invalid(form)

    def form_invalid(self, form):
        if not form.is_valid():
            return redirect('schedulesDisplay')
        return self.render_to_response(self.get_context_data(form=form))


@method_decorator(login_required, name='dispatch')
class ScheduleUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app.can_view_schedule'
    model = Schedule
    form_class = ScheduleForm
    template_name = 'cloud_scheduling/scheduleUpdate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = get_object_or_404(Schedule, pk=self.kwargs['pk'])
        context['nfe'] = NFe.objects.filter(idSchedule=schedule)
        context['form_a'] = ListNfeForm(initial={'id_schedule': schedule.pk})
        context['form_b'] = ListNfeForm(initial={'id_schedule': schedule.pk})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_a = ListNfeForm(request.POST)
        if form_a.is_valid():
            form_a.save()
        context = self.get_context_data(form_a=form_a)
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        if 'nfe_id' in kwargs:
            return self.nfe_delete(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def nfe_delete(self, request, *args, **kwargs):
        nfe_id = kwargs['nfe_id']
        nfe = get_object_or_404(NFe, pk=nfe_id)
        nfe.delete()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.request.path


@permission_required('app.can_view_schedule')
def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    return redirect('schedulesDisplay')  # Redireciona para a página de lista de schedules


@permission_required('app.can_view_schedule')
def nfe_delete(request, nfe_id):
    nfe = get_object_or_404(NFe, pk=nfe_id)
    nfe.delete()
    # return redirect('scheduleUpdate')  # Redireciona para a página de lista de schedules


# Fim da Lista de Agendamentos
################################
# Views da Lista de Fornecedores

class CompanySupplierListView(PermissionRequiredMixin, FilterView):
    permission_required = 'app.can_view_schedule'
    model = CompanySupplier
    filterset_class = CompanySupplierFilter
    paginate_by = 20
    template_name = 'cloud_scheduling/companySupplierListDisplay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supplier_list = self.get_queryset()
        paginator = Paginator(supplier_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            supplier_list_paginator = paginator.page(page)
        except PageNotAnInteger:
            supplier_list_paginator = paginator.page(1)
        except EmptyPage:
            supplier_list_paginator = paginator.page(paginator.num_pages)

        context['supplier_list'] = supplier_list_paginator
        context['form'] = CompanySupplierForm
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form_a = CompanySupplierForm(request.POST)

            if form_a.is_valid():
                form_a.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form_a.errors})
        else:
            return super().post(request, *args, **kwargs)


class CompanySupplierNew(PermissionRequiredMixin, FormView):
    permission_required = 'app.can_view_schedule'
    form_class = CompanySupplierForm
    template_name = 'cloud_scheduling/companySupplierListDisplay.html'
    success_url = 'company_supplier_new'

    def form_valid(self, form):
        form_a = form.save(commit=False)
        if form.is_valid():  # Verifica a validade do formulário
            form_a.save()
            return redirect('companySupplierListDisplay')
        return super().form_invalid(form)

    def form_invalid(self, form):
        if not form.is_valid():
            return redirect('companySupplierListDisplay')
        return self.render_to_response(self.get_context_data(form=form))


class CompanySupplierUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app.can_view_schedule'
    model = CompanySupplier
    form_class = CompanySupplierForm
    template_name = 'cloud_scheduling/companySupplierUpdate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_supplier = get_object_or_404(CompanySupplier, pk=self.kwargs['pk'])

        context['form_a'] = ContactCompanySupplierForm(initial={'id_company': company_supplier.pk})
        context['form_b'] = AddressCompanySupplierForm(initial={'id_company_supplier': company_supplier.pk})

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_a = ContactCompanySupplierForm(request.POST)
        form_b = AddressCompanySupplierForm(request.POST)
        if form_a.is_valid() and form_b.is_valid():
            form_a.save()
            form_b.save()
        context = self.get_context_data(form_a=form_a)
        context_ = self.get_context_data(form_a=form_a)
        return self.render_to_response(context, context_)


@permission_required('app.can_view_schedule')
def company_supplier_delete(request, company_supplier_id):
    company_supplier = get_object_or_404(CompanySupplier, pk=company_supplier_id)
    company_supplier.delete()
    return redirect('companySupplierListDisplay')  # Redireciona para a página de lista de Fornecedores


# Fim da Lista de Fornecedores
################################

# Views da Lista de Transportadoras

class CompanyShippingListView(PermissionRequiredMixin, FilterView):
    permission_required = 'app.can_view_schedule'
    model = CompanyShippingTransport
    filterset_class = CompanyShippingTransportFilter
    paginate_by = 20
    template_name = 'cloud_scheduling/companyShippingListDisplay.html'

    # companyShippingUpdate
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shipping_list = self.get_queryset()
        paginator = Paginator(shipping_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            shipping_list_paginator = paginator.page(page)
        except PageNotAnInteger:
            shipping_list_paginator = paginator.page(1)
        except EmptyPage:
            shipping_list_paginator = paginator.page(paginator.num_pages)

        context['shipping_list'] = shipping_list_paginator
        context['form'] = CompanyShippingListForm
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form_a = CompanyShippingListForm(request.POST)

            if form_a.is_valid():
                form_a.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form_a.errors})
        else:
            return super().post(request, *args, **kwargs)


class CompanyShippingNew(PermissionRequiredMixin, FormView):
    permission_required = 'app.can_view_schedule'
    form_class = CompanyShippingListForm
    template_name = 'cloud_scheduling/companyShippingListDisplay.html'
    success_url = 'company_shipping_new'

    def form_valid(self, form):
        form_a = form.save(commit=False)
        if form.is_valid():  # Verifica a validade do formulário
            form_a.save()
            return redirect('companyShippingListDisplay')
        return super().form_invalid(form)

    def form_invalid(self, form):
        if not form.is_valid():
            return redirect('companyShippingListDisplay')
        return self.render_to_response(self.get_context_data(form=form))


class CompanyShippingUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app.can_view_schedule'
    model = CompanyShippingTransport
    form_class = CompanyShippingListForm
    template_name = 'cloud_scheduling/companyShippingUpdate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_shipping = get_object_or_404(CompanyShippingTransport, pk=self.kwargs['pk'])

        context['form_a'] = ContactCompanyShippingForm(initial={'id_company': company_shipping.pk})
        context['form_b'] = AddressCompanyShippingForm(initial={'id_company': company_shipping.pk})

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_a = ContactCompanyShippingForm(request.POST)
        form_b = AddressCompanyShippingForm(request.POST)
        if form_a.is_valid() and form_b.is_valid():
            form_a.save()
            form_b.save()
        context = self.get_context_data(form_a=form_a)
        context_ = self.get_context_data(form_a=form_b)
        return self.render_to_response(context, context_)


@permission_required('app.can_view_schedule')
def company_shipping_delete(request, company_shipping_id):
    company_shipping = get_object_or_404(CompanyShippingTransport, pk=company_shipping_id)
    company_shipping.delete()
    return redirect('companyShippingListDisplay')  # Redireciona para a página de lista de Transportadora

# Fim da Lista de Transportadora
