from django.contrib import admin
from django.contrib.auth import get_user_model
# モデルをインポート
from . models import Student, Lesson, Message

# 管理ツールに登録
Teacher = get_user_model()
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Message)
