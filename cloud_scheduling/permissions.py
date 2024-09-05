from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import Schedule, ScheduleStatus
from django.contrib.auth.models import Group


ct_view_schedule = ContentType.objects.get_for_models(Schedule, ScheduleStatus)  # Substitua "Schedule" pelo seu modelo
pm_view_schedule = Permission.objects.create(
    codename='can_view_schedule',
    name='Can View Schedule',
    content_type=ct_view_schedule,
)
# a tag name se registra o grupo a se usado no bloqueio da função
gp_view_schedule = Group.objects.get(name='Agendamento')
gp_view_schedule.permissions.add(pm_view_schedule)
