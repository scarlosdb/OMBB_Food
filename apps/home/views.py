from django.shortcuts import render
from django.http import HttpResponse
# from apps.blog.models import Blog


# Create your views here.
def home(request):
    # query = None
    # query_dict = request.GET
    # query = query_dict.get("q")
    # if query is not None:
    #     # blogs = Blog.objects.get(id=query)
    #     blogs = Blog.objects.all()
    # else:
    #     blogs = Blog.objects.all()
    context = {
        'home': home
    }
    return render(request, 'home/home.html', context)


