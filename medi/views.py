from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,'signup.html')

def index1(request):
	abc = request.GET.get('email1','default')
	print(abc)
	return render(request,'resistered.html')
	# return HttpResponse(abc)

def index2(request):
	return render(request,'login.html')