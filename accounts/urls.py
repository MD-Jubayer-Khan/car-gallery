from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.User_login.as_view(), name='login'),
    path('logout/', views.User_logout.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile')
]
