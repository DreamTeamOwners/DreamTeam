from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import views_group
from apps.users.views import views_comment
from apps.users.views.views import *

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='token'),

    path('profile_detail/<int:id>/', ProfileDetailAPIView.as_view(), name='profile_detail'),
    path('my_profile_detail/', MyProfileAPIView.as_view(), name='my_profile_detail'),
    path('profile_update/', ProfileUpdateAPIView.as_view(), name='profile_update'),

    path('group_create/', views_group.CreateGroupAPIView.as_view()),
    path('group_list/', views_group.GroupListAPIView.as_view()),
    path('group_detail/<int:pk>/', views_group.GroupDetailAPIView.as_view()),
    path('group_update/<int:pk>/', views_group.GroupUpdateAPIView.as_view()),
    path('group_delete/<int:pk>/', views_group.GroupDeleteAPIView.as_view()),

    path('user_list/', SearchAPIView.as_view(), name='users'),

    path('comment/', views_comment.CommentCreateAPIView.as_view()),
    path('comment_update/<int:pk>/', views_comment.CommentUpdateAPIView.as_view()),
    path('comment_delete/<int:pk>/', views_comment.CommentDeleteAPIView.as_view()),
]
