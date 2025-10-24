# users/views.py
from rest_framework import viewsets
from routes.models import UserRoute, Segment
from .serializers import UserRouteSerializer, SegmentSerializer

class UserRouteViewSet(viewsets.ModelViewSet):
    queryset = UserRoute.objects.all()
    serializer_class = UserRouteSerializer

class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer