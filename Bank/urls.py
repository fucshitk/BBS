"""Bank URL Configuration

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
from django.conf import settings
from django.conf.urls import url,include
from django.views.static import serve

import xadmin
from django.contrib import admin
from App import views
from App.views import *

from Bank.settings import MEDIA_ROOT
from ueditor import urls as d_urls

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^bbs/',include('App.urls',namespace='app')),
    url(r'^ueditor/',include(d_urls,namespace='d_urls')),
    # url(r'^likes/', include('likes.urls')),
    url(r'^$', views.index, name='index'),

    url(r'^terminal_svr', views.terminal_svr,name='terminal_svr'),


]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)