from django.db import models

class ChallengeAPI(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'home_product'

    def __str__(self):
        return self.name