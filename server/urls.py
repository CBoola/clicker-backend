from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
router = routers.DefaultRouter()



urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('homepage.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler404 = 'homepage.views.main_page'
handler500 = 'homepage.views.main_page'