
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='accounts'

urlpatterns = [
    path('profile/', views.profile,name="profile"),
    path('register/', views.register,name="register"),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/<int:pk>/update', views.update_profile, name='update_profile'),
]
