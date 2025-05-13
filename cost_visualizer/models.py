# Create your models here.
from django.db import models

class CostHistory(models.Model):
    account_count = models.PositiveIntegerField()
    regular_cost = models.FloatField()
    compressed_cost = models.FloatField()
    savings = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_count} accounts: ${self.savings} saved"