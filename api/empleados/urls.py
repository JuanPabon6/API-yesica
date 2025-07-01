from rest_framework import routers
from django.urls import path,include
from .views import EmpleadosViewSets

router = routers.DefaultRouter()
router.register(r'', EmpleadosViewSets)

urlpatterns = [
    path('', include(router.urls))
]

