"""sampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from user.api.add_activity_period.views_add_activity_period import AddActivatityPeriodAPI
from user.api.add_user.views_add_user import AddUserAPI
from user.api.get_all_user.views_get_all_users import GetallUserAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^addActivatityPeriod/$', AddActivatityPeriodAPI.as_view()),
    url(r'^addUser/$', AddUserAPI.as_view()),
    url(r'^getallUser/$', GetallUserAPI.as_view()),

]
