from .forms import NewUserForm, SuggestionForm
from .models import HotfixLog

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView


@login_required
def index(request):
    hotfix_form = HotfixLog.objects.all().order_by('-pk')[:5]
    version = HotfixLog.objects.all().order_by('-pk').first()
    form_a = SuggestionForm(request.POST)

    if request.method == "POST":
        if form_a.is_valid():
            form_a.save()

    return render(request, 'cloud_home/index.html', {
        'hotfix_form': hotfix_form,
        'vs': version,
        'form_a': form_a,
    })

@permission_required('app.can_use_register')
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="cloud_home/register.html", context={"register_form": form})


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset_form.html'
