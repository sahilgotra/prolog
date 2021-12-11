from django.urls import path
from.import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.userlogout, name='logout'),

]
