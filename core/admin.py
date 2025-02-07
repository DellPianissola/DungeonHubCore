from django.contrib import admin

from core.user.admin.admin import User, UserAdmin


admin.site.register(User, UserAdmin)
