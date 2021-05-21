from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.PostListView.as_view(), name="post list"),
    path("post_details", views.PostDetailView.as_view(), name="post details"),
]
