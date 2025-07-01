from rest_framework import routers
from django.urls import path,include
from .views import PagosViewSets

router = routers.DefaultRouter()
router.register(r'', PagosViewSets)

urlpatterns = [
    path('', include(router.urls))
]
