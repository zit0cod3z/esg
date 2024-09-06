from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header ="Login to ESG Registration Portal"
admin.site.site_title ="Welcome to ESG REGISTRATION dashboard"
admin.site.index_title ="Welcome to ESG's Dashboard"

urlpatterns = [
    path('', views.register, name="register"),
]