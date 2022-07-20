from django.urls import path
from api import views

urlpatterns = [
    path('', views.article_list),
    path('<int:id>', views.article_details),
    
]