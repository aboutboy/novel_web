# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views


app_name = 'novel_site'
urlpatterns = [
    url(r'^$', cache_page(60 * 15)(views.HomeView.as_view()), name='home'),
    url(r'^cate/quanben/$', views.QuanbenView.as_view(), name='quanben'),
    url(r'^cate/(?P<cate>[a-z]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^info/(?P<pk>[0-9]+)/$', views.InfoView.as_view(), name='info'),
    url(r'^book/(?P<pk>[0-9]+)/(?P<index>[0-9]+)/$', views.BookView.as_view(), name='detail'),
    url(r'^search', views.SearchView.as_view(), name='search'),
    url(r'^test', views.SearchTest.as_view(), name='test'),
    url(r'^404$', views.page_not_found, name='404')
]

