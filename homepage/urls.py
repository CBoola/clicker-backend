from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^home$', views.main_page)
]
