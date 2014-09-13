from django.conf.urls import patterns, url

from participants import views

urlpatterns = patterns('',
    url(r'^text/', views.recieve_text, name='recieve_text'),
    url(r'^$', views.index, name='index'),
)