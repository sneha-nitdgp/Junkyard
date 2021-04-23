
from django.urls import path,include
from . import views

urlpatterns = [
   path('index.html/', views.get_question, name="get_question"),
   
   
   
]
