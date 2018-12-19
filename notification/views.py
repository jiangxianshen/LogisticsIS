from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Notification


def detail(request, article_id):
    if request.user.is_authenticated:
        blogs = get_object_or_404(Notification, id=article_id)
        infer = request.GET.get('infer')
        content = {"blogs": blogs, 'infer':infer}
        return render(request, "notification_detail.html", content)
    else:
        return redirect('login')


def notification(request, page_num):
    if request.user.is_authenticated:
        page = Paginator(Notification.objects.filter(recommend=False), per_page=10)
        articles = page.page(page_num)
        top_articles = Notification.objects.filter(recommend=True)
        content = {"articles": articles, "top_articles":top_articles, 'page_num':page_num, 'count':page.count//10+1}
        return render(request, "notification.html", content)
    else:
        return redirect('login')

