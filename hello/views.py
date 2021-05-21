from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from hello.models import Post


def home(request):
    return HttpResponse("Hello, Django!")


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
