from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('login',login, name="login"),
    path('signup',signup,name="signin"),
    path('services/',services,name="services"),
    path('display/',display,name="display"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)