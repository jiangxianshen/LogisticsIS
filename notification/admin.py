from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Notification
# Register your models here.


@admin.register(Notification)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ("title", "recommend", "publish_time")
    ordering = ("publish_time",)