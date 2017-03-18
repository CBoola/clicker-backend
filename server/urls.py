from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views

from rest_framework import routers
router = routers.DefaultRouter()



urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

    url(r'^api/', include(router.urls)),
    url(r'^', include('homepage.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler404 = 'homepage.views.main_page'
handler500 = 'homepage.views.main_page'