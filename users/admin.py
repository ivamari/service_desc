from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal info', {
            'fields': ('username', 'first_name', 'last_name', 'middle_name',
                       'email', 'password')
        }),
        ('Permissions', {
            'fields': ('role', 'is_staff', 'is_superuser', 'is_active'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )
    list_display = ('id', 'first_name', 'last_name', 'email', 'role', 'is_staff',
                    'is_active', 'is_superuser')
    list_display_links = ('first_name', 'last_name', 'email', )

    search_fields = ('first_name', 'last_name', 'email', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role')
