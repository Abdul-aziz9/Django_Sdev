from django.urls import path
from . import views  # Import the view function

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing posts
]
