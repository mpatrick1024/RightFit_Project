from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^register_form$', views.register_form),
    url(r'^login_form$', views.login_form),
    url(r'^profile$', views.profile),
    url(r'^accountpage$', views.accountpage),
    url(r'^account_edit_form$', views.account_edit_form),
    url(r'^loading$', views.loading),
    url(r'^schoolchoices$',views.schoolchoices),
    url(r'^schoolmatches$',views.schoolmatches), 
]