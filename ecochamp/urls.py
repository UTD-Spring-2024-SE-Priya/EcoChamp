from django.urls import path
from ecochamp import views

# Associates each function in views.py to a URL path
# Empty "" means default path (will change to landing page later)
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
]