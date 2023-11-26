from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "reg_date"]


admin.site.register(User, UserAdmin)
