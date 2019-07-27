"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url


from organizer import urls as organizer_urls
from app1 import urls as app1_urls
from .views import redirect_root


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include(organizer_urls)),
    re_path('ˆblog/', include(app1_urls)),
    url(r'^$', redirect_root),
]
