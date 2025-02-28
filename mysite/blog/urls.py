from django.urls import path
from . import views  # Import the view function

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing posts
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]
