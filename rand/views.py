from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import random
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewUserForm


@csrf_exempt
def rand_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return HttpResponse(random.randint(1000, 9999))
    form = AuthenticationForm()
    return render(request=request, template_name="randgenerator/login.html", context={"login_form": form})


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("rand")
    form = NewUserForm()
    return render(request=request, template_name="randgenerator/register.html", context={"register_form": form})
