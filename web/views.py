import os
from django.shortcuts import render
from web.forms import RegistrationForm
from web.models import User


def main_view(request):
    return render(request, os.path.join("web", "main.html"))


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
            print(form.cleaned_data)
    return render(request, os.path.join("web", "registration.html"), {"form": form, "is_success": is_success})
