from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate/$', views.validate),
    url(r'^login/$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^wish_items$', views.wish_items),
    url(r'^wish_items/create_item$', views.create_item, name='add_item'),
    url(r'^wish_item/(?P<id>\d+)/display$', views.display),
    url(r'^wish_item/(?P<id>\d+)/remove$', views.remove, name='remove'),
    url(r'^wish_item/(?P<id>\d+)/delete$', views.delete, name='delete'),
    url(r'^logout$', views.logout)
]
