from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='user_signup'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
    path('book-slot/<int:center_id>/', views.book_slot, name='book_slot'),
]
