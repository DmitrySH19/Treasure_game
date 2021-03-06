from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

default = {'header': 'Костыль', 'login_button': 'Enter', 'registration_button': 'Registration'}

def user_login(request):
    if request.method == 'POST':
        if 'Login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        if 'Registration' in request.POST:
            return HttpResponsePermanentRedirect("/account/registration/")
    else:
        form = LoginForm()
        data = default
        # noinspection PyTypeChecker
        data.update({'form': form})
        return render(request, 'index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return HttpResponse("success")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration.html', {'user_form': user_form})