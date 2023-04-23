from django.contrib import admin
from .models import HomeGroup, Floor


class HomeGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'family_code',
        'build_year',
        'build_material',
        'id',
    )
    search_fields = (
        'family_code',
    )

    list_per_page = 25
    # exclude = ('id', )
    # ordering = ('-build_year',)


class FloorAdmin(admin.ModelAdmin):
    list_display = (

        'id',
        'number',
        'safe_zone'
    )

    list_per_page = 25
    # exclude = ('id', )
    # ordering = ('-build_year',)


admin.site.register(HomeGroup, HomeGroupAdmin)
admin.site.register(Floor, FloorAdmin)
