from django.contrib import admin

from core.user.admin.admin import UserAdmin
from core.user.models.user import User


admin.site.register(User, UserAdmin)
