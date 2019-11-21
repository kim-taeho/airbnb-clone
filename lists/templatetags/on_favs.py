from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    user = context.request.user
    the_list = list_models.List.objects.get_or_none(
        user=user, name="My Favourite Houses"
    )
    if the_list is None:
        return False
    else:
        return room in the_list.rooms.all()
