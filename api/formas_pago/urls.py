from rest_framework import routers
from django.urls import path,include
from .views import FormasPagosViewSets

router = routers.DefaultRouter()
router.register(r'', FormasPagosViewSets)

urlpatterns = [
    path('', include(router.urls))
]
