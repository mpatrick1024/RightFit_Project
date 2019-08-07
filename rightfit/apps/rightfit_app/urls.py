from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^accountpage$', views.accountpage),
    url(r'^account_edit_form$', views.account_edit_form),
    url(r'^loading$', views.loading),
    url(r'^schoolchoices$',views.schoolchoices),
    
]