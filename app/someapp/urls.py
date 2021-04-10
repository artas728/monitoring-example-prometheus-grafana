from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^save_to_redis/$', views.save_to_redis, name='save_to_redis'),
    url(r'^sync_endpoint/$', views.endpoint, name='endpoint'),
    url(r'^write_to_db/$', views.write_to_db, name='write_to_db'),
]