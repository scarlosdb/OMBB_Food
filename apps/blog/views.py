from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from apps.blog.models import Blog
from .forms import BlogForm

# Create your views here.


def blog_view(request):
    blogs = Blog.objects.all()


# def blog_search(request):
#     context = {
#
#     }
#     return render(request, 'blog/search.html', context=context)

@login_required
def create_blog(request):
    initial_data = {
         "blog_date": datetime.now(),

    }
    form = BlogForm(request.POST or None, initial=initial_data)
    context = {
        "form": form
    }

    if form.is_valid():
        blog = form.save()
        context['blog'] = BlogForm





        # title = request.POST.get("blog_title")
        # content = request.POST.get("blog_content")
        # # private = request.POST.get("blog_private")
        # if request.POST.get("private") == 'on':
        #     private = True
        # else:
        #     private = False
        # date = datetime.now()
        # if private:
        #     context['private'] = 'on'
        # else:
        #     context['private'] = 'off'
        # context['blog_date'] = date
    return render(request, "blog/create_blog.html", context=context)
