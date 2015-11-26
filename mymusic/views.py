from django.shortcuts import render
from forms import UserDetailsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from models import Userdetails
from django.template import RequestContext

# Create your views here.

def home(request):
	return render(request,'home.html')

def signup(request):
	print request.POST
	form = UserDetailsForm()
	if request.POST:
		form = UserDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			HttpResponseRedirect('mymusic/home')
	return render_to_response('signup.html',{'form':form}, context_instance=RequestContext(request))
# def signin(request):