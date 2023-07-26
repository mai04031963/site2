from django.urls import path
from . import views

urlpatterns = [
    path('new_demand/',views.new_demand, name="new_demand"),
    path('', views.service, name="comments")
    ]