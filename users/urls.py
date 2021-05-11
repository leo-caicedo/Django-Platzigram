# Django
from django.urls import path

# Views
from users.views import login_view, logout_view, signup_view

name_app = 'users'
urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('me/profile', signup_view, name='update_profile'),
]
