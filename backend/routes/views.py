# routes/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserRoute
from .serializers import UserRouteSerializer

@api_view(['POST'])
def create_route(request):
    if not request.user.is_authenticated:
        return Response({"error": "Требуется авторизация"}, status=status.HTTP_401_UNAUTHORIZED)

    from_point = request.data.get("from")
    to_point = request.data.get("to")

    if not from_point or not to_point:
        return Response({"error": "Укажите начальную и конечную точку маршрута"}, status=status.HTTP_400_BAD_REQUEST)

    # Формируем имя маршрута
    route_name = f"{from_point} - {to_point}"

    # Создаем маршрут
    route = UserRoute(
        user=request.user,
        name=route_name,
        general_start_point=from_point,
        general_end_point=to_point
    )
    route.save()

    serializer = UserRouteSerializer(route)
    return Response({"route": serializer.data}, status=status.HTTP_201_CREATED)