from django.urls import path
from apps.resume.views import views_resume

urlpatterns = [
    path('', views_resume.ResumeCreateView.as_view()),
    path('my_resume/', views_resume.MyResumeView.as_view()),

]
