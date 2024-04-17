from django.urls import path
from ecochamp import views

# Associates each function in views.py to a URL path
# Empty "" means default path (will change to landing page later)
urlpatterns = [
    path("", views.start, name="start"),
    path("home/", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path("login/", views.user_login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("avatar/", views.avatar, name="avatar"),
    path("help/", views.help, name="help"),
    path("faq/", views.faq, name="faq")
]