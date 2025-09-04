from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = (
        ("new", "New"),
        ("paid", "Paid"),
        ("canceled", "Canceled"),
    )
    user = models.ForeignKey(
        "core.User",  # строковая ссылка вместо прямого импорта
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    booking_expiry = models.DateTimeField(null=True, blank=True)
    group_booking_id = models.IntegerField(null=True, blank=True)
    price_applied = models.JSONField(default=dict)


class BookingPricing(models.Model):
    booking = models.ForeignKey(
        "core.Booking",
        on_delete=models.CASCADE,
        related_name="pricing"
    )
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)


class BookingDetail(models.Model):
    booking = models.ForeignKey(
        "core.Booking",
        on_delete=models.CASCADE,
        related_name="details"
    )
    seat_class = models.CharField(max_length=50)
    luggage_info = models.TextField(blank=True)


class BookingHistory(models.Model):
    booking = models.ForeignKey(
        "core.Booking",
        on_delete=models.CASCADE,
        related_name="history"
    )
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="changed_bookings"
    )
    change_type = models.CharField(max_length=50)
    old_status = models.CharField(max_length=50, blank=True)
    new_status = models.CharField(max_length=50)


class Ticket(models.Model):
    booking = models.ForeignKey(
        "core.Booking",
        on_delete=models.CASCADE,
        related_name="tickets"
    )
    passenger_name = models.CharField(max_length=255)
    seat_number = models.CharField(max_length=20, blank=True)
    issued_at = models.DateField()
    schedule_id = models.IntegerField()  # FK → schedules.id


class Payment(models.Model):
    booking = models.ForeignKey(
        "core.Booking",
        on_delete=models.CASCADE,
        related_name="payments"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    paid_at = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    refund_status = models.CharField(max_length=50, blank=True)
    transaction_id = models.CharField(max_length=255, blank=True)
    payment_gateway = models.CharField(max_length=100, blank=True)
    loyalty_points_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserFile(models.Model):
    user = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="files"
    )
    booking = models.ForeignKey(
        "core.Booking",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="files"
    )
    review_id = models.IntegerField(null=True, blank=True)  # FK → reviews.id
    file_url = models.TextField()
    file_type = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)

