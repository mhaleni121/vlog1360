from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path(r'^login/$', LoginView.as_view(template_name="users/login.html"), name='login'),
    # logout_view
    path(r'^logout/$', views.logout_view, name='logout'),
    # Registration page
    path(r'^register/$', views.register, name='register'),
 ]
