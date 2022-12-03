from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Lesson, Message

Teacher = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = [Teacher.USERNAME_FIELD] + Teacher.REQUIRED_FIELDS + ['password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class IsCheckedForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['is_checked']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['date','time', 'teacher', 'student', 'subject']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['person', 'message']