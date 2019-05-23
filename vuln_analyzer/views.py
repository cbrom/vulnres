import zipfile
import argparse
from django.shortcuts import render
from tokenapi.decorators import token_required

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.utils import timezone
from vuln_analyzer.models import Vulnerability, File, Patch
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
@token_required
def index(request):
	print(request.method)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			# handle file here
			ret = form.save(commit=False)
			ret.owner = User.objects.all()[0]
			ret.file_name = "feilename"
			ret.unzip_path = "path"
			ret.save()

			with open('better.json') as f:
				data = json.load(f)

			dump = json.dumps(data)

			return JsonResponse(data)
		else:
			return HttpResponse(form)
	else:
		form = UploadFileForm()
	
	return HttpResponse(request.method == 'POST')
	
def unzip_file(file_name):
	output_directory = "test_zip"
	zip_file = zipfile.ZipFile(file_name, "r")
	zip_file.extractall(output_directory)
	zip_file.close()