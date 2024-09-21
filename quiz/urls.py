from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.logins, name="logins"),
    path('test', views.userhome, name="userhome"),
    path('register', views.userregister, name="userregister"),
    path('test/<int:value>', views.Qustionhome, name="Qustionhome"),
    path('result', views.Result, name="Result"),
    path('showview', views.Fullbiew, name="Fullbiew"),
    path('dash', views.dashbord, name="dashbord"),
    path('logout', views.logout, name="logout"),
    path('resultlist', views.resultbl, name="resultbl"),
               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)