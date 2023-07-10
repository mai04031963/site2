from django.shortcuts import render, redirect
from . models import Comments
from django.views.generic import ListView, CreateView
from . forms import CommentForm, CommentForm2


class CommentsListView(ListView):
    model = Comments
    template_name = "comments/comments.html"
    paginate_by = 5
    allow_empty = True

    def get(self, request, *args, **kwargs):
        return super(CommentsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Comments.objects.all().order_by("-id", "-comment_date")


def new_comment(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('../')
        else:
            context = {'form': form}
            return render(request, 'comments/new_comment.html', context)
    else:
        form = CommentForm()
        context = {'form': form}
        return render(request, 'comments/new_comment.html', context)


def new_comment2(request):

    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            context = {'form': form}
            return render(request, 'comments/new_comment2.html', context)
    else:
        form = CommentForm2()
        context = {'form': form}
        return render(request, 'comments/new_comment2.html', context)
