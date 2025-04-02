from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_view, name='predict'),
    path('about/', views.about, name='about'),
    path('services/', views.bot_page, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('update-user/', views.updateUser, name="update-user"),
]
