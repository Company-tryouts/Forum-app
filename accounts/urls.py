from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    # signup
    path('signup/', views.signup, name='signup'),

    # login / logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # password change (user must be logged in)
    path('settings/password/', auth_views.PasswordChangeView.as_view(
            template_name='password_change.html',
            success_url=reverse_lazy('password_change_done')),
         name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'),
         name='password_change_done'),
]
