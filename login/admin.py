from django.contrib import admin
from .models import ManagerUser, RegisterCode
# Register your models here.


@admin.register(ManagerUser)
class UserAdmin(admin.ModelAdmin):

    list_display = ("username", )

@admin.register(RegisterCode)
class CodeAdmin(admin.ModelAdmin):

    list_display = ("code", "is_new")