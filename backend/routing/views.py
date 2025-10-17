
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def find_routes(request):
    # Получаем данные из запроса
    from_point = request.data.get('from')
    to_point = request.data.get('to')

    # Если что-то не заполнено, возвращаем ошибку
    if not from_point or not to_point:
        return Response({"error": "Необходимо указать начальную и конечную точку маршрута"}, status=status.HTTP_400_BAD_REQUEST)

    # Ответ с полученными данными
    routes = [
        {"id": 1, "start": from_point, "end": to_point, "message": f"Маршрут: {from_point} -> {to_point}"},
        {"id": 2, "start": from_point, "end": to_point, "message": f"Маршрут: {from_point} -> {to_point}"},
    ]
    
    return Response({"routes": routes}, status=status.HTTP_200_OK)
