from django.shortcuts import render, redirect
from . models import Good, Category
from django.http import Http404
from django.views.generic import ListView
from . forms import GoodsForm


class GoodsListView(ListView):
    model = Good
    template_name = "goods/goods.html"
    paginate_by = 100
    allow_empty = True
    filter = ''

    def get(self, request, *args, **kwargs):
        return super(GoodsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Good.objects.all().order_by("id")
#def index(request):
#    form = GoodsForm()
#    context = {'form': form}
#    return render(request, "goods/cat1.html", context)


def detail(request, _id):
    try:
        good = Good.objects.get(pk=_id)
    except Good.DoesNotExist:
        raise Http404("Good does not exist")
    return render(request, "goods/detail.html", {"good": good.name, "id": good.id, "description": good.description})


def goods_list(request):

    form = GoodsForm()
    context = {'form': form}
    if request.method == 'GET':
        print("произошел get запрос")
    if request.method == 'POST':
        print('произошел POST запрос')
    return render(request, "goods/goods_seek.html", context)


