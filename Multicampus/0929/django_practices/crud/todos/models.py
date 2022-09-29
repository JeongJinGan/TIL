from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Todo(models.Model):
    # django에서 pk(id)는 자동으로 만들어준다.
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=80)
    """
    # default :
    데이터를 생성할 대 값을 안넣으면
    자동으로 값을 채워서 데이터를 생성하겠다.
    """
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
