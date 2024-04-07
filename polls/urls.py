from django.urls import path
from polls.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='list-view-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail-view-post'),
    path('create/', PostCreateView.as_view(), name='post-create-view' ),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post-update-view'),
    path('edit/<int:pk>/', PostDeleteView.as_view(), name='post-delete-view')
]
