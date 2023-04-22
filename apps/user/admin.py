from django.contrib import admin

from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'userId',
                    'is_superuser', 'is_active', 'is_configured', 'last_login')
    list_display_links = ('email', )
    search_fields = ('email', 'username'
                     )
    list_filter = ('is_superuser', 'is_active', 'is_configured')

    list_per_page = 25
    exclude = ('password', 'last_login', 'date_joined',
               'groups', 'user_permissions', 'active')
    ordering = ('-created_on',)
    readonly_fields = ('is_superuser', 'is_active', 'is_staff')


admin.site.register(User, UserAdmin)
