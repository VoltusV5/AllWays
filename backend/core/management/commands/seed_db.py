"""
Management command to seed the database with initial mock data.
Usage: python manage.py seed_db
"""

from django.core.management.base import BaseCommand
from core.models import User
from routes.models import UserRoute, Segment

class Command(BaseCommand):
    help = 'Seeds the database with initial dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting database seeding...")

        # Пользователи
        user1, created1 = User.objects.get_or_create(email="user1@example.com")
        if created1:
            user1.set_password("12345")
            user1.save()
            self.stdout.write(self.style.SUCCESS(f"Created user: {user1.email}"))
        else:
            self.stdout.write(self.style.WARNING(f"User {user1.email} already exists."))
        
        user2, created2 = User.objects.get_or_create(email="user2@example.com")
        if created2:
            user2.set_password("12345")
            user2.save()
            self.stdout.write(self.style.SUCCESS(f"Created user: {user2.email}"))
        else:
            self.stdout.write(self.style.WARNING(f"User {user2.email} already exists."))

        # Пример маршрута
        route, created_route = UserRoute.objects.get_or_create(
            user=user1,
            name="Test Route",
            defaults={
                "general_start_point": "Moscow",
                "general_end_point": "St. Petersburg"
            }
        )
        if created_route:
            self.stdout.write(self.style.SUCCESS(f"Created route: {route.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Route {route.name} already exists."))

        # Пример сегмента
        segment, created_segment = Segment.objects.get_or_create(
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
        if created_segment:
            self.stdout.write(self.style.SUCCESS("Created Segment 1"))
        else:
            self.stdout.write(self.style.WARNING("Segment 1 already exists."))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
