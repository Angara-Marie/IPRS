from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSets


router = routers.DefaultRouter()
router.register(r"customers", CustomerViewSets)
urlpatterns= [
    path("", include(router.urls))
]