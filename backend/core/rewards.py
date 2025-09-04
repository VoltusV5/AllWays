from django.db import models

class Reward(models.Model):
    REWARD_TYPES = (
        ("promo", "Promo"),
        ("loyalty", "Loyalty"),
    )
    type = models.CharField(max_length=20, choices=REWARD_TYPES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PromoReward(models.Model):
    reward = models.ForeignKey(
        "core.Reward",
        on_delete=models.CASCADE,
        related_name="promo_rewards"
    )
    coupon_code = models.CharField(max_length=50)
    valid_until = models.DateTimeField()
    usage_limit = models.IntegerField(default=1)


class LoyaltyReward(models.Model):
    reward = models.ForeignKey(
        "core.Reward",
        on_delete=models.CASCADE,
        related_name="loyalty_rewards"
    )
    earn_rate = models.DecimalField(max_digits=5, decimal_places=2)
    redeem_rate = models.DecimalField(max_digits=5, decimal_places=2)
    min_points_required = models.IntegerField(default=0)


class UserLoyaltyBalance(models.Model):
    user = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        related_name="loyalty_balance"
    )
    points_balance = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
