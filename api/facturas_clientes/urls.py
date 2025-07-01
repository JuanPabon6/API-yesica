from rest_framework import routers
from django.urls import path,include
from .views import FacturasDeClientesViewSets

router = routers.DefaultRouter()
router.register(r'', FacturasDeClientesViewSets)

urlpatterns = [
    path('', include(router.urls))
]
