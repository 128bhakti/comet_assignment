from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . forms import RegistrationForm

def index(request):
	form= RegistrationForm()
	context={
		"myregistrationform": form
	}
	return render(request,"assignment/index.html",context)