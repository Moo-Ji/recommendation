from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
	url(r'^$', views.index),
    path('result/', views.index01),
    path('result01/', views.index02),
    path('result02/', views.index03),
    path('result03/', views.index04),
    path('result04/', views.index05),
]
