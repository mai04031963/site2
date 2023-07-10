from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentsListView.as_view(), name="comments"),
    path('new_comment/', views.new_comment2, name="new_comment")
    ]
