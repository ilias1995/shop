from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'apps.smartshop.views.index', name='index'),
	url(r'^(?P<id>\d+)/$', 'apps.smartshop.views.info', name='info'),
	url(r'^smartshop/', include('apps.smartshop.urls')),
	(r'^shop/', include('shop.urls')),
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
