from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=50)
    content = MDTextField(default="")
    publish_time = models.DateTimeField(auto_now_add=True)  # 日期，新增自动写入
    recommend = models.BooleanField(default=False) #置顶

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        # 排序
        ordering = ['-publish_time']