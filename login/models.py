from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def uuid_hex():
    '''
    uuid生成十六进制注册码
    '''
    return uuid.uuid1().hex


# Create your models here.
class ManagerUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        pass


class RegisterCode(models.Model):

    code = models.CharField(primary_key=True, default=uuid_hex, max_length=32, editable=False)
    is_new = models.BooleanField(default=True, editable=False)
