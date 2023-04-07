from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import views_group
from apps.users.views import views_comment
from apps.users.views import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='register'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view(), name='token'),

    path('profile_detail/<int:id>/', views.ProfileDetailAPIView.as_view(), name='profile_detail'),
    path('my_profile_detail/', views.MyProfileAPIView.as_view(), name='my_profile_detail'),
    path('profile_update/', views.ProfileUpdateAPIView.as_view(), name='profile_update'),

    path('group_create/', views_group.CreateGroupAPIView.as_view()),
    path('group_list/', views_group.GroupListAPIView.as_view()),
    path('group_detail/<int:pk>/', views_group.GroupDetailAPIView.as_view()),
    path('group_update/<int:pk>/', views_group.GroupUpdateAPIView.as_view()),
    path('group_delete/<int:pk>/', views_group.GroupDeleteAPIView.as_view()),

    path('user_search/', views.UserSearchAPIView.as_view(), name='users'),
    path('group_search/', views.GroupSearchView.as_view()),

    path('groups/<int:group_id>/', views_group.GroupAddAPIView.as_view()),
    path('group_remove/<int:group_id>/', views_group.GroupRemoveAPIView.as_view()),

    path('comment/<int:group_id>/', views_comment.CommentCreateAPIView.as_view()),
    path('comment_update/<int:pk>/', views_comment.CommentUpdateAPIView.as_view()),
    path('comment_delete/<int:pk>/', views_comment.CommentDeleteAPIView.as_view()),
]
