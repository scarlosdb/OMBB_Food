from django.urls import path
from . import views

urlpatterns = [

    path('create_blog/', views.create_blog, name='create_blog'),

]