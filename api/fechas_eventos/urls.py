from rest_framework import routers
from django.urls import path, include
from .views import FechasEventosViewSets

router = routers.DefaultRouter()
router.register(r'', FechasEventosViewSets)

urlpatterns = [
    path('', include(router.urls))
]
