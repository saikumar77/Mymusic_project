from django.conf.urls import  patterns, include, url 

urlpatterns = patterns('',
	url(r'^home/$','mymusic.views.home'),
	url(r'^signup/$','mymusic.views.signup'),
	url(r'^signin/$','mymusic.views.signin'),
	)