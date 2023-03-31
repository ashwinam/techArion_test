from django.urls import path
from app_student import views

urlpatterns = [
    path('', views.StudentApiView.as_view())
]
