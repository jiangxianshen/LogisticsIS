from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:page_num>', views.notification, name="notification"),
    path('detail/<int:article_id>', views.detail, name='detail'),
]