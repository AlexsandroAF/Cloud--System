from django.contrib import admin
from .models import Account, Departament, Group, Company, HotfixLog


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_email', 'account_dtcreate', 'account_depart', 'account_group')
    list_filter = ('account_depart', 'account_group')
    search_fields = ('account_name', 'account_email')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('fantasy_name', 'corporate_name', 'registration_number', 'description')


class HotfixLogAmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'version', 'date_create')
    list_filter  = ('title', 'details', 'version')
    search_fields = ('title', 'version')


admin.site.register(Company, CompanyAdmin)

admin.site.register(Account, AccountAdmin)

admin.site.register(Departament)

admin.site.register(Group)

admin.site.register(HotfixLog, HotfixLogAmin)
