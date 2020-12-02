from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('result/<int:question_id>/', views.result, name='result'),
    path('vote/<int:question_id>/', views.vote, name='vote'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
