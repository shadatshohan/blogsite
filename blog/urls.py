from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('',PostListView.as_view(),name="blog_home"),
    path('posts/new/',PostCreateView.as_view(),name="blog_create"),
    path('posts/<int:pk>/update/',PostUpdateView.as_view(),name="blog_update"),
    path('posts/<int:pk>/delete/',PostDeleteView.as_view(),name="blog_delete"),
    path('posts/<int:pk>/',PostDetailView.as_view(),name="blog_detail"),
    path('about/',views.about,name="blog_about"),
    path('user/<str:username>',UserPostListView.as_view(),name='user_posts')
]