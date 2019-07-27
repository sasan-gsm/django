from django.conf.urls import url, re_path
from django.urls import path

from .views import homepage, tag_detail, startup_list, startup_detail, tag_list

urlpatterns = [

    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    url(r'^$', homepage),
    url(r'^tag/$', tag_list, name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail')

]
