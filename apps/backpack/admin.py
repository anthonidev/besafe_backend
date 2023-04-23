from django.contrib import admin

from .models import Element


class ElementAdmin(admin.ModelAdmin):
    list_display = (

        'name',
        'description',
        'type'
    )

    list_per_page = 25


admin.site.register(Element, ElementAdmin)
