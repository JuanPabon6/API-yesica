from rest_framework import routers
from django.urls import path, include
from .views import DetallesVentasViewSets

router = routers.DefaultRouter()
router.register(r'', DetallesVentasViewSets)

urlpatterns = [
    path('', include(router.urls))
]
