from rest_framework import routers
from django.urls import path,include
from .views import TematicasViewSets

router = routers.DefaultRouter()
router.register(r'',TematicasViewSets)

urlpatterns = [
    path('', include(router.urls))
]
