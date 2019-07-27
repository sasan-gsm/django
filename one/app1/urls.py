from django.conf.urls import url
from .views import PostList, post_detail

urlpatterns = [
    url(r'ˆ$', PostList.as_view(), {'parent_template': 'base.html'}, name='app1_post_list'),
    url(r'ˆ(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail, name='app1_post_detail'),
]