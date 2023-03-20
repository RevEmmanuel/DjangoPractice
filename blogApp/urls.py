from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('simi/', views.simi, name='simi'),
    # path('', views.home, name='home'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]
