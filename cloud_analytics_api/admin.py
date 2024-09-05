from django.contrib import admin
from .models import (ApiCloudDash000001,
                     ApiCloudDash000002,
                     ApiCloudDash000003,
                     ApiCloudDash000004,
                     ApiCloudDash000004)


# Register your models here.
class RankingVendasAdmin(admin.ModelAdmin):
    list_display = (
        'vendedor',
        'vlrvda',
        'custovda',
        'vlrdev',
        'vdaliq',
        'custoliq',
        'margem',
        'direto',
        'lucro',
        'perclucro'
    )


admin.site.register(ApiCloudDash000001, RankingVendasAdmin)
