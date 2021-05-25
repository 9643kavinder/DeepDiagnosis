from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout/<int:id>', views.logout, name="logout"),
    path('get_profile/<int:id>', views.get_profile, name="get_profile"),
    path('update_profile/<int:id>', views.update_profile, name="update_profile"),
    path('find_labs', views.find_labs, name="find_labs"),
]