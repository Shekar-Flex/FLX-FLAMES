# from nis import match
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('match',views.match,name='match')
]