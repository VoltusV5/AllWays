from core.models import User
from routes.models import UserRoute, Segment

def run():
    # Пользователи
    user1, _ = User.objects.get_or_create(email="user1@example.com")
    user1.set_password("12345")
    user1.save()
    
    user2, _ = User.objects.get_or_create(email="user2@example.com")
    user2.set_password("12345")
    user2.save()

    # Пример маршрута и сегмента
    route, _ = UserRoute.objects.get_or_create(
        user=user1,
        name="Test Route",
        defaults={
            "general_start_point": "Moscow",
            "general_end_point": "St. Petersburg"
        }
    )
    Segment.objects.get_or_create(
        user_route=route,
        segment_number=1,
        defaults={
            "name": "Segment 1",
            "start_point_lat": 55.7558,
            "start_point_lon": 37.6173,
            "end_point_lat": 59.9343,
            "end_point_lon": 30.3351,
            "duration": 240,
            "distance_km": 700,
            "transport_type": "Train",
            "price": 5000
        }
    )

    print("База заполнена")