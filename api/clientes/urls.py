from django.urls import path,include
from rest_framework import routers
from .views import ClientesViewSets

router = routers.DefaultRouter()
router.register(r'', ClientesViewSets)

urlpatterns = [
    path('',  include(router.urls))
]

