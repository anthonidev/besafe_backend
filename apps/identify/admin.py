from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'dni',
    )
    search_fields = (
        'dni',
    )

    list_per_page = 25
    exclude = ('id', )
    ordering = ('-dob',)


admin.site.register(Account, AccountAdmin)
