from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRM = "confirm"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRM, "Confirm"),
        (STATUS_CANCELED, "Canceled")
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in} "