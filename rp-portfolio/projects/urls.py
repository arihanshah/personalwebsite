from django.urls import path
from . import views

urlpatterns = [
    # path("", views.project_index, name="project_index"),
    path("", views.homepage, name="homepage"),
    path("blog", views.blog, name="blog"),
    path("single_blog", views.single_blog, name="single_blog")
    # path("<int:pk>/", views.project_detail, name="project_detail"),
]