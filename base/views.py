from django.shortcuts import render
from .models import Post
# Example dynamic data
from datetime import date

# Tailwinds CSS homepage
def homepage(request):
    post_list = Post.objects.all()
    context = {}
    context['post_list'] = post_list
    print(context)
    return render(request, 'base.html', context)
