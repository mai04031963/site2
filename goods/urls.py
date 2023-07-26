from django.urls import path, re_path
from . views import good_search2, index

urlpatterns = [
    path("", good_search2, name='catalogs'),
    path("<int:_id1>/", good_search2, name='catalogs1'),
    path("<int:_id1>/<int:_id2>/", good_search2, name='catalogs2'),
    path("<int:_id1>/<int:_id2>/<int:_id3>/", good_search2, name='catalogs3'),
    path("index<int:_id>/", index, name='index'),
    path("<int:_id1>/index<int:_id>/", index, name='index1'),
    path("<int:_id1>/<int:_id2>/index<int:_id>/", index, name='index2'),
    path("<int:_id1>/<int:_id2>/<int:_id3>/index<int:_id>/", index, name='index3'),
]


