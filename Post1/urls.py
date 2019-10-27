from django.urls import path
from . import views
urlpatterns = [
    path('', views.list, name='projects'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('new/',views.PostCreateView.as_view(template_name='post/new_post.html'),name='post_new')]