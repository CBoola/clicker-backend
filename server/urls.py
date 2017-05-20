from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'player', views.PlayerViewSet)
router.register(r'structure', views.StructureViewSet)
router.register(r'upgrade', views.UpgradeViewSet)
router.register(r'achievement', views.AchievementViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('homepage.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='API docs'))
]

handler404 = 'homepage.views.main_page'
handler500 = 'homepage.views.main_page'