from django.shortcuts import render
from django.views import generic
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.db.models import Q
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetails(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def search(request):
  query = request.GET.get('q')
  print(query)
  posts = Post.objects.filter(Q(title__icontains=query),Q(content__icontains=query))
  print(posts)
  return render(request, 'search-result.html', {'posts': posts})



