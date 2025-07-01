from rest_framework import routers
from django.urls import path,include
from .views import MaterialesViewSets

router = routers.DefaultRouter()
router.register(r'', MaterialesViewSets)

urlpatterns = [
    path('', include(router.urls))
]
