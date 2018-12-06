from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from django.core.paginator import Paginator
from .models import Notification
import markdown


def detail(request, article_id):
    blogs = get_object_or_404(Notification, id=article_id)
    infer = request.GET.get('infer')
    blogs.content = markdown.markdown(blogs.content,
                                      extension=[
                                          #缩写，表格等
                                          'markdown.extensions.extra',
                                      ])
    content = {"blogs": blogs, 'infer':infer}
    return render(request, "notification_detail.html", content)


def notification(request, page_num):
    page = Paginator(Notification.objects.filter(recommend=False), per_page=10)
    articles = page.page(page_num)
    top_articles = Notification.objects.filter(recommend=True)
    content = {"articles": articles, "top_articles":top_articles, 'page_num':page_num, 'count':page.count//10+1}
    return render(request, "notification.html", content)

