from django.contrib import admin
from django.contrib.auth import get_user_model
# モデルをインポート
from . models import Student
from . models import Lesson

# 管理ツールに登録
Teacher = get_user_model()
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Lesson)
