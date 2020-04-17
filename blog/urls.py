from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.listing, name='posts'),
    path('post/<int:id>/', views.detail, name='detail'),
    path('post/add/', views.add_post, name='add_post'),
]
