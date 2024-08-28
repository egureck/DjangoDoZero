from django.urls import path
from polls.views import (
     index, ola, 
     QuestionCreateView, question_create,
     QuestionUpdateView, question_update)
    
urlpatterns = [
    path('index/', index, name='index'),
    path('ola', ola, name='ola'),
    path('enquete/add', QuestionCreateView.as_view(), name="poll_add"),
    path('quest/create', question_create, name="poll_cre"),
    path('enq/<int:pk>/edit', QuestionUpdateView.as_view(), name="quest_upd"),
    path('enq/<int:question_id>/update', question_update, name="quest_updF"),
]