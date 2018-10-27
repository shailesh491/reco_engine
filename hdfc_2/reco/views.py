from django.shortcuts import render

# Create your views here.
from .models import property
	

def all(request):
	context = {'Property':property.objects.all()}
	template = 'base.html'
	return render(request, template, context)

def single(request, id):
	props = property.objects.get(id = id)
	context = {'Propertys':props}
	template = 'property_page.html'
	return render(request, template, context)