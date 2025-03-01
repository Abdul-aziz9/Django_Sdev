from django.urls import path
from . import views  # Import the view function

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing posts
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('new/', views.post_new, name='post_new'),
]
