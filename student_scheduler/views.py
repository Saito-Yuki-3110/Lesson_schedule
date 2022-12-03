from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models
from .form import SignupForm, LoginForm, IsCheckedForm, LessonForm, MessageForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
import pytz

# Create your views here.
#ログイン
class TeacherLogin(LoginView):

    form_class = LoginForm

    template_name = 'Login.html'

#ログアウト
class TeacherLogout(LoginRequiredMixin, LogoutView):
    template_name = 'Logout.html'

#デフォルト(ホーム)画面
class Teacher(LoginRequiredMixin, TemplateView):
    #Messageテーブル連携
    model = models.Message
    #テンプレートファイル連携
    template_name = 'Teacher.html'
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "message"
    #時間設定
    jst = pytz.timezone('Asia/Tokyo')
    today = datetime.now(tz=jst)
    #contextデータ設定
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['today']= self.today
        return context


#一覧画面(教師)
class TeacherList(ListView):
    #Teacherテーブル連携
    model = models.Teacher
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "teacher_list"
    #テンプレートファイル連携
    template_name = "Teacher_list.html"

#一覧画面(生徒)
class StudentList(ListView):
    #Studentテーブル連携
    model = models.Student
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "student_list"
    #テンプレートファイル連携
    template_name = "Student_list.html"

#一覧画面(授業)
class LessonList(ListView):
    #Lessonテーブル連携
    model = models.Lesson
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "lesson_list"
    #テンプレートファイル連携
    template_name = "Lesson_list.html"

    jst = pytz.timezone('Asia/Tokyo')
    today = datetime.now(tz=jst)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today']= self.today
        return context

#詳細画面(教師)
class TeacherDetail(DetailView):
    #Teacherテーブル連携
    model = models.Teacher
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "teacher_detail"
    #テンプレートファイル連携
    template_name = "Teacher_detail.html"

#詳細画面(生徒)
class StudentDetail(DetailView):
    #Studentテーブル連携
    model = models.Student
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "student_detail"
    #テンプレートファイル連携
    template_name = "Student_detail.html"

#詳細画面(授業)
class LessonDetail(DetailView):
    #Lessonテーブル連携
    model = models.Lesson
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "lesson_detail"
    #テンプレートファイル連携
    template_name = "Lesson_detail.html"

    jst = pytz.timezone('Asia/Tokyo')
    today = datetime.now(tz=jst)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today']= self.today
        return context

#新規登録(教師)
class TeacherSignup(CreateView):

    template_name = 'Teacher_form.html'

    form_class = SignupForm

    def get_success_url(self):
        return reverse('Scheduler:list1')
    
#新規登録画面(生徒)
class StudentCreateView(CreateView):
    #Studentテーブル連携
    model = models.Student
    #入力項目定義
    fields = ("name","age","subject","teacher")
    #テンプレートファイル連携
    template_name = "Student_form.html"
    #作成後のリダイレクト先
    def get_success_url(self):
        return reverse('Scheduler:list2')

#新規登録画面(授業)
class LessonCreateView(CreateView):
    #Lessonテーブル連携
    model = models.Lesson
    #テンプレートファイル連携
    template_name = "Lesson_form.html"

    form_class = LessonForm

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['initial'] = {'teacher': self.request.user} 
        return form_kwargs

    #作成後のリダイレクト先
    def get_success_url(self):
        return reverse('Scheduler:list')

#更新画面(教師)
class TeacherUpdateView(UpdateView):

    model = models.Teacher

    form_class = SignupForm
    #テンプレートファイル連携
    template_name = "Teacher_form.html"
    #更新後のリダイレクト先
    success_url = reverse_lazy("Scheduler:list1")

#更新画面(生徒)
class StudentUpdateView(UpdateView):
    #入力項目定義
    fields = ("name","age","subject","teacher")
    #Studentテーブル連携
    model = models.Student
    #テンプレートファイル連携
    template_name = "Student_form.html"
    #更新後のリダイレクト先
    success_url = reverse_lazy("Scheduler:list2")

#更新画面(授業)
class LessonUpdateView(UpdateView):
    #入力項目定義
    fields = ("date","time","teacher","student","subject")
    #Lessonテーブル連携
    model = models.Lesson
    #テンプレートファイル連携
    template_name = "Lesson_form.html"
    #更新後のリダイレクト先
    success_url = reverse_lazy("Scheduler:list")

#授業確認画面
class LessonIsCheckedView(UpdateView):

    model = models.Lesson

    context_object_name = "lesson_detail"

    template_name = "LessonIsChecked_form.html"

    form_class = IsCheckedForm

    success_url = reverse_lazy("Scheduler:list")

    def get_initial(self):
            initial = super().get_initial()
            initial["is_checked"] =  True
            return initial

#削除画面(教師)
class TeacherDeleteView(DeleteView):
    #Studentテーブル連携
    model = models.Teacher
    #テンプレートファイル連携
    template_name = "Teacher_delete.html"
    #削除後のリダイレクト先
    success_url = reverse_lazy("Scheduler:list")

#削除画面(生徒)
class StudentDeleteView(DeleteView):
    #Studentテーブル連携
    model = models.Student
    #テンプレートファイル連携
    template_name = "Student_delete.html"
    #削除後のリダイレクト先
    success_url = reverse_lazy("Scheduler:list")

#削除画面(授業)
class LessonDeleteView(DeleteView):
    #Lessonテーブル連携
    model = models.Lesson
    #テンプレートファイル連携
    template_name = "Lesson_delete.html"
    #削除後のリダイレクト先
    success_url = reverse_lazy("Scheduler:list")

#お知らせフォーム画面
class MessageFormView(CreateView):
    #Messageテーブル連携
    model = models.Message
    #テンプレートファイル連携
    template_name = "Message.html"
    #フォーム連携
    form_class = MessageForm
    #初期値設定
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['initial'] = {'person': self.request.user} 
        return form_kwargs
    #作成後のリダイレクト先
    def get_success_url(self):
        return reverse('Scheduler:list')
