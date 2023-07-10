from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from . models import News
from django.http import Http404
from django.views.generic import ListView


# Create your views here.
def news(request):
    news_list = News.objects.all()
    context = {"news_list": news_list,}
    return render(request, "news/news.html", context)


class NewsListView(ListView):
    model = News
    template_name = "news/news.html"
    #queryset = Comments.objects.all().order_by("-comment_date")
    paginate_by = 8
    allow_empty = True

    def get(self, request, *args, **kwargs):
        return super(NewsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.all().order_by("-news_date")