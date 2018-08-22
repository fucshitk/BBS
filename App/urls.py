from django.conf.urls import url,include
from django.contrib import admin

from App import views
urlpatterns = [
    url(r'register/',views.register,name='register'),
    url(r'login/',views.login,name='login'),
    url(r'logout/',views.logout,name='logout'),
    url(r'mine/',views.mine,name='mine'),

    url(r'getvcode',views.getvcode,name='getvcode'),

    url(r'shici/',views.shici,name='shici'),
    url(r'sanwen/',views.sanwen,name='sanwen'),
    url(r'xiaoshuo/',views.xiaoshuo,name='xiaoshuo'),
    url(r'yuyan/',views.yuyan,name='yuyan'),
    url(r'tonghua/',views.tonghua,name='tonghua'),
    url(r'rizhi/',views.rizhi,name='rizhi'),
    url(r'duanzi/',views.duanzi,name='duanzi'),
    url(r'chuishui/',views.chuishui,name='chuishui'),


    url(r'addact/',views.addact,name='addact'),
    url(r'set/',views.set,name='set'),

    url(r'readart/(\d+)/',views.readart,name='readart'),

    url(r'ta/(\d+)/',views.ta,name='ta'),

    # url(r'^like/(?P<pk_id>\d+)/(?P<obj_type>[\w+]+)/$', views.like, name ='like'),

    url(r'search/',views.search,name='search'),

    url(r'about/',views.about,name='about'),




]

