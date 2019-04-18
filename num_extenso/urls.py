from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from core.viewset import NumeroViewSet

router = routers.DefaultRouter()
router.register(r'', NumeroViewSet, base_name='numero')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
