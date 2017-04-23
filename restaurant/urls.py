from django.conf.urls import url

from . import views

app_name = 'restaurant'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Restaurant_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^CustomerRegister/$', views.CustomerRegister, name='CustomerRegister'),
]
