from django.urls import path
from . views import GoodsListView, goods_list

urlpatterns = [
    path("", goods_list, name="index"),
    # ex: /goods/5/
    #path("<int:_id>/", views.detail, name="detail"),
    # ex: /goods/5/results/
    #path("<int:_id>/results/", views.results, name="results"),
    # ex: /goods/5/vote/
    #path("<int:_id>/vote/", views.vote, name="vote")
]