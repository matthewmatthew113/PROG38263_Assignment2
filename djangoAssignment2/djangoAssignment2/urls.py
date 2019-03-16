"""djangoAssignment2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Import Django Various Django Libraries including user_views from users
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

#URLs for administration, registration, login/logout, and password reset
urlpatterns = [
    path('admin/', admin.site.urls),
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
	path('reset-password/done', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_success.html'), name='password_reset_done'),
	path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_password_confirmation.html'), name='password_reset_confirm'),
	path('', include('blog.urls')),
	path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('', include('blog.urls')),
]
