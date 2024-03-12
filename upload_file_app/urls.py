from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, welcome, logout_view, home, download_file, delete_file

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', logout_view, name='logout'), 
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
    # Add other URLs as needed
]