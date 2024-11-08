from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    # Query all posts, order by the latest created
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})
