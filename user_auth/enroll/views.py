from django.shortcuts import render
from .forms import loginform

# Create your views here.
def log_in(request):
    if request.method == "POST":
        frm = loginform(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = loginform()
    return render(request, 'login.html',{'form': frm})