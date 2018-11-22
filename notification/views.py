from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Notification


def detail(request, article_id):
    blogs = get_object_or_404(Notification, id=article_id)
    content = {"blogs": blogs}
    return render(request, "detail.html", content)


def notification(request):
    articles = Notification.objects.filter(recommend=False)
    top_articles = Notification.objects.filter(recommend=True)
    content = {"articles": articles, "top_articles":top_articles}
    return render(request, "notification.html", content)

