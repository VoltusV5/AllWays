from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'routes', views.UserRouteViewSet)
router.register(r'segments', views.SegmentViewSet)

