from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^(?P<nameproduct_id>\d+)/$', 'apps.smartshop.views.detail', name='detail'),
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
)