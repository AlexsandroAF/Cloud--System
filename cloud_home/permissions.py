from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

from .models import Account

ct_register = ContentType.objects.get_for_model(Account)
pm_register = Permission.objects.create(
    codename='can_use_register',
    name='Can Register New Users',
    content_type=ct_register,
)

gp_register_view = Group.objects.get(name='Administrator') or Group.objects.get(name='Moderador')
gp_register_view.permissions.add(pm_register)
