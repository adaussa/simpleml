from django.shortcuts import render
from django.core import management
from .models import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
import subprocess
# Create your views here.

def ImageRecognition(request):

	if request.method == "POST" and request.FILES['imagePost']:
		myfile = request.FILES['imagePost']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)

		subprocess.call(['./darknet detect cfg/yolov3.cfg yolov3.weights /home/armand/Projectes/SimpleML/simpleml/media/'+myfile.name], shell=True, cwd='/home/armand/Projectes/SimpleML/darknet')
		subprocess.call(['cp predictions.jpg /home/armand/Projectes/SimpleML/simpleml/media/predictions/'+myfile.name], shell=True, cwd='/home/armand/Projectes/SimpleML/darknet')
		subprocess.call(['rm '+myfile.name], shell=True, cwd='/home/armand/Projectes/SimpleML/simpleml/media/')
		
		predicted = True
		file = "predictions/"+myfile.name

		return render(request, 'detection.html', {'file' : file, 'predicted' : predicted})
	else:
		predicted = False
		return render(request, 'detection.html', {'predicted' : predicted})