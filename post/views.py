from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

# Create your views here.

def home_view(request):
    posts_qs = Post.objects.all().order_by('-id')

    paginator = Paginator(posts_qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home-view.html", {"page_obj": page_obj})

def single_post_view(request, id):

    post = Post.objects.get(id = id)

    return render(request, 'post.html', {"post": post})
