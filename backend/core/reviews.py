from django.db import models

class RouteReview(models.Model):
    route = models.ForeignKey(
        "core.Route",  # строковая ссылка на модель Route
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        "core.User",  # строковая ссылка на модель User
        on_delete=models.CASCADE,
        related_name="route_reviews"
    )
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewFile(models.Model):
    review = models.ForeignKey(
        "core.RouteReview",
        on_delete=models.CASCADE,
        related_name="files"
    )
    file_url = models.TextField()
    file_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)
