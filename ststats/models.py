from django.db import models
from django.db.models import JSONField


# Create your models here.
class Player(models.Model):
    account_creation_date = models.DateTimeField()
    display_name = models.TextField()

    def __str__(self):
        return str(self.display_name)

    def serialize(self):
        return {
            "account_creation_date": self.account_creation_date,
            "display_name": self.display_name
        }


class Run(models.Model):
    upload_date = models.DateTimeField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    data = JSONField()

    def __str__(self):
        return str(self.upload_date)
