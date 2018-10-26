from django.contrib import admin
from .models import ManagerUser
# Register your models here.


@admin.register(ManagerUser)
class UserAdmin(admin.ModelAdmin):

    list_display = ("username", )