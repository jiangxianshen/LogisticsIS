from django.db import models

# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()  # Text长文本字段，可以写很多内容
    publish_time = models.DateTimeField(auto_now_add=True)  # 日期，新增自动写入
    recommend = models.BooleanField(default=False) #置顶

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        # 排序
        ordering = ['-publish_time']