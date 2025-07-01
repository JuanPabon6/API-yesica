from django.urls import path,include
from rest_framework import routers
from .views import TiposDeEventosViewSets

router = routers.DefaultRouter()
router.register(r'', TiposDeEventosViewSets)

urlpatterns = [
    path('', include(router.urls))
]
