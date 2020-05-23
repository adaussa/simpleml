from django.shortcuts import render
from django.core import management
from .models import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
# Create your views here.

def ImageRecognition(request):

	filepath = request.FILES.get('filepath', False)

	if (filepath!=False):
		return HttpResponse("Hola1")
	else:
		return HttpResponse("Hola")