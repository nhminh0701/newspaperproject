from django.urls import path
from newspaper import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<test>/', views.ArticleListView.as_view(), name='test'),
]