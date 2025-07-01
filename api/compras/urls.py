from rest_framework import routers
from django.urls import path,include
from .views import ComprasViewSets

router = routers.DefaultRouter()
router.register(r'', ComprasViewSets)

urlpatterns = [
    path('',  include(router.urls))
]
