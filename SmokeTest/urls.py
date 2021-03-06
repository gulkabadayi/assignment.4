
"""SmokeTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from assignment3.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Teacher_adding/$', Teacher_Adding),
    url(r'^Course_Adding/$', Course_Adding),
    url(r'^Student_Adding/$', Student_Adding),
    url(r'^All_courses/$', All_courses),
    url(r'^All_teachers/$', All_teachers),
    url(r'^All_students/$', All_students),
]
