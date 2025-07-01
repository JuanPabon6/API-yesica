from django.urls import path,include
from rest_framework import routers
from .views import VentasViewSets

router = routers.DefaultRouter()
router.register(r'', VentasViewSets)

urlpatterns = [
    path('', include(router.urls))
]
