from django import template
import datetime
from reservations import models as reservations_models

register = template.Library()


@register.simple_tag()
def is_booked(room, day):
    if day.number == 0:
        return 
    else:
        try:
            date = datetime.datetime(year=day.year, month=day.month, day=day.number)
            reservations_models.BookedDay.objects.get(day=date, reservation__room=room)
            return True
        except reservations_models.BookedDay.DoesNotExist:
            return False