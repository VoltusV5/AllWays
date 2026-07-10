"""
Views для приложения routes.
"""

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserRoute
from .serializers import UserRouteSerializer


class RouteCreateAPIView(APIView):
    """
    Создание нового маршрута пользователя.
    Ожидает POST-запрос с JSON телом, содержащим поля `from` и `to`.
    """
    
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        from_point = request.data.get("from")
        to_point = request.data.get("to")

        if not from_point or not to_point:
            return Response(
                {"error": "Укажите начальную (from) и конечную (to) точки маршрута."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        route = UserRoute.objects.create(
            user=request.user,
            name=f"{from_point} - {to_point}",
            general_start_point=from_point,
            general_end_point=to_point
        )

        serializer = UserRouteSerializer(route)
        return Response({"route": serializer.data}, status=status.HTTP_201_CREATED)