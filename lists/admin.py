from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "count_rooms"
    )

    search_fields = ("name",)

    filter_horizontal = ("rooms",)
