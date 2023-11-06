from django.db import models


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True, null=False, auto_created=True, unique=True)
    username = models.CharField(max_length=32, null=False)
    pwd = models.CharField(max_length=64, null=False)

    # 可以添加其他自定义方法
    @staticmethod # 定义静态方法， 不需要self
    def get_all():
        # 计算年龄的逻辑
        user_list = [
            {
                'id': 1,
                'username': 'jack',
                'pwd': '123456'
            },
            {
                'id': 2,
                'username': 'tom',
                'pwd': '123456'
            }
        ]
        return user_list
