from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'incidents', views.IncidentViewSet)
router.register(r'systemapps', views.SystemAppViewSet)
router.register(r'roles', views.AccountViewSet)
router.register(r'sessions', views.SessionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
