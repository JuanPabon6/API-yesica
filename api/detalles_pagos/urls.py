from rest_framework import routers
from django.urls import path,include
from .views import DetallePagosViewSets

router = routers.DefaultRouter()
router.register(r'', DetallePagosViewSets)

urlpatterns = [
    path('', include(router.urls))
]
