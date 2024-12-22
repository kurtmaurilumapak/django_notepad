from django.urls import path
from . import views

urlpatterns = [
    path('add_note/', views.add_note_view, name='add_note'),
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
