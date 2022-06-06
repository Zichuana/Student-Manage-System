from django.db import models

# Create your models here.

# 1.创建模型类
# 创建用户类
class UserInfo(models.Model):
# 2.定义字段 属性
   UserId = models.AutoField(primary_key=True)
   username = models.CharField(max_length=16, blank=False, verbose_name="用户名")
   password = models.CharField(max_length=16, blank=False, verbose_name="密码")


# 创建学生信息类
class StuInfo(models.Model):
   id = models.CharField(max_length=16, primary_key=True)
   stuname = models.CharField(max_length=16, verbose_name="学生姓名")
   stuphone = models.CharField(max_length=16, verbose_name="学生电话")
   stuaddress = models.CharField(max_length=16, verbose_name="学生地址")
   stucollege = models.CharField(max_length=16, verbose_name="学生院系")
   stumajor = models.CharField(max_length=16, verbose_name="学生专业")
# Create your models here.


class Course(models.Model):
   cno = models.CharField(max_length=16, primary_key=True)
   cname = models.CharField(max_length=16, verbose_name="课程名")
   cpno = models.CharField(max_length=16, verbose_name="先修课程", null=True)
   ccredit = models.IntegerField(default=60, verbose_name="课程学分")


class sc(models.Model):
   sid = models.ForeignKey('StuInfo', on_delete=models.CASCADE)
   scno = models.ForeignKey('Course', on_delete=models.CASCADE)
   grade = models.IntegerField(default=60, verbose_name='课程分数')
   class Meta:
      unique_together = ("sid", "scno")


# python manage.py makemigrations
# python manage.py migrate

