from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Teacher(AbstractUser):
    age     = models.PositiveIntegerField(verbose_name="年齢")
    subject = models.CharField(choices=settings.HI_SUB_CHOICE,max_length=5,verbose_name="教科")
    date_joined = None
    REQUIRED_FIELDS = ["email", "age", "subject"]

class Student(models.Model):
    name    = models.CharField(max_length=30,default="名前",verbose_name="名前")
    age     = models.PositiveIntegerField(verbose_name="年齢")
    subject = models.CharField(choices = settings.HI_SUB_CHOICE,max_length=5,verbose_name="教科")
    teacher = models.ForeignKey(Teacher,related_name='Student',on_delete=models.CASCADE,verbose_name="担当教師")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    date = models.DateField(default=date.today,verbose_name="授業日")
    time = models.CharField(choices=settings.TIME_CHOICE,max_length=5,verbose_name="授業開始時間")
    teacher = models.ForeignKey(Teacher,related_name='Lesson',on_delete=models.CASCADE,verbose_name="教師")
    student = models.ForeignKey(Student,related_name='Lesson',on_delete=models.CASCADE,verbose_name="生徒")
    subject = models.CharField(choices=settings.HI_SUB_CHOICE,max_length=5,verbose_name="教科")
    is_checked = models.BooleanField(default=False)

    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=["date","time", "teacher"],
                    name="dt_teacher_unique"
                ),
                models.UniqueConstraint(
                    fields=["date","time","student"],
                    name="dt_student_unique"
                ),
            ]

class Message(models.Model):
    message = models.CharField(max_length=150, default="メッセージを記入",blank=False,verbose_name="お知らせ")
    person = models.ForeignKey(Teacher,related_name='Message',on_delete=models.CASCADE,verbose_name="教師")