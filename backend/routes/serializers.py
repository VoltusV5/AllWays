# users/serializers.py
from rest_framework import serializers
from routes.models import UserRoute, Segment

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = '__all__'

class UserRouteSerializer(serializers.ModelSerializer):
    segments = SegmentSerializer(many=True, read_only=True)

    class Meta:
        model = UserRoute
        fields = ['id', 'user', 'name', 'general_start_point', 'general_end_point', 'segments']