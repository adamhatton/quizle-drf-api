from django.urls import path
from quizzes import views

urlpatterns = [
    path('quizzes/', views.QuizList.as_view()),
    path('quizzes/<int:pk>/', views.QuizDetail.as_view()),
]
