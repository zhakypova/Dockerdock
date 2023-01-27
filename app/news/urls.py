from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.NewsListCreateAPIView.as_view()),
    path('<int:pk>/', views.NewsRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:news_id>/comment/', views.CommentListCreateAPIView.as_view()),
    path('<int:news_id>/comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('status/', views.StatusListCreateAPIView.as_view()),
    path('status/<int:pk>/', views.StatusRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:news_id>/<str:slug>/', views.StatusNewsCreateAPI.as_view()),
]