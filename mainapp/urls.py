from rest_framework.routers import DefaultRouter

from .views import LocationModelViewSet, CharacterModelViewSet, EpizodeModelViewSet

routers = DefaultRouter()

routers.register('location', LocationModelViewSet)
routers.register('character', CharacterModelViewSet)
routers.register('epizod', EpizodeModelViewSet)

urlpatterns = routers.urls