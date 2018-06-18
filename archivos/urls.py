from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import public_page

urlpatterns = [
       url(r'^$', public_page, name='public_page'),
]