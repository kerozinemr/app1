from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    
    path('login/',views.loginPage, name="login"),
    path('register/',views.register, name="register"),
    path('logout/',views.logoutUser, name="logout"),
    
    path('profile/',views.profile, name="profile"), 
    path('',views.home, name='home'),
    path('About/',views.about),
    path('Contact/',views.contact),
    
    path('create_task/',views.createTask,name="create_task"),
    path('update_task/<str:pk>/',views.UpdateTask,name="update_task"),
    path('delete_task/<str:pk>/',views.deleteTask,name="delete_task"),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_sent.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_form.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_done.html'), name='password_reset_complete'),


  
   

]


