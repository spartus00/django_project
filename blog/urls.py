from django.urls import path
from . import views         # the "." is the current directory

urlpatterns = [
    path('', views.home, name='blog-home'),  # the '' is the homepage. The view that handles the logic is the home view from the homeview module.
    path('about/', views.about, name='blog-about')
]

