from django.urls import path
from scores import views

urlpatterns = [
    path('scores/', views.ScoreList.as_view()),
    path('scores/<int:pk>/', views.ScoreDetail.as_view()),
]
