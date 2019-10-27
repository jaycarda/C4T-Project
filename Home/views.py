from django.shortcuts import render
from .form import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def profile(request):
        return render(request, 'pages/user_home.html')
