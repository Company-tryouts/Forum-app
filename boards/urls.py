from django.contrib import admin
from django.urls import path, re_path
from boards import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('about/', views.about, name='about'),
    path('new_post/', views.NewPostView.as_view(), name='new_post'),

]
