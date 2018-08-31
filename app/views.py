from django.shortcuts import render
from .forms import ReservaForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'app/login.html')
    else:
        form = ReservaForm(request.POST or None)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
        context = {
            "form":form
            }
    return render(request, 'app/index.html', context)