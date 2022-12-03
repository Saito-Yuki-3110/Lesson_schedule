#path関数をインポート
from django.urls import path
# 同ディレクトリからview.pyをインポート
from . import views

#アプリ名を定義
app_name = "Scheduler"

urlpatterns = [
    path('signup/', views.TeacherSignup.as_view(), name='signup'),                 #新規登録画面(教師)
    path('login/', views.TeacherLogin.as_view(), name='login'),                    #ログイン画面
    path('logout/', views.TeacherLogout.as_view(), name='logout'),                 #ログアウト画面
    path('', views.Teacher.as_view(), name='list'),                            #ホーム画面  
    path('teacherlist/', views.TeacherList.as_view(), name='list1'),               #一覧画面(教師)
    path('studentlist/', views.StudentList.as_view(), name='list2'),               #一覧画面(生徒)
    path('lessonlist/', views.LessonList.as_view(), name='list3'),                 #一覧画面(授業)
    path('detail1/<int:pk>/',views.TeacherDetail.as_view(),name='detail1'),        #詳細画面(教師)
    path('detail2/<int:pk>/',views.StudentDetail.as_view(),name='detail2'),        #詳細画面(生徒)
    path('detail3/<int:pk>/',views.LessonDetail.as_view(),name='detail3'),         #詳細画面(生徒)
    path('create2/',views.StudentCreateView.as_view(),name='create2'),             #新規登録画面(生徒)
    path('create3/',views.LessonCreateView.as_view(),name='create3'),              #新規登録画面(授業)
    path('update1/<int:pk>/',views.TeacherUpdateView.as_view(),name='update1'),    #更新画面(教師)
    path('update2/<int:pk>/',views.StudentUpdateView.as_view(),name='update2'),    #更新画面(生徒)
    path('update3/<int:pk>/',views.LessonUpdateView.as_view(),name='update3'),     #更新画面(授業)
    path('check/<int:pk>/',views.LessonIsCheckedView.as_view(),name='check'),     #授業確認画面(授業)
    path('delete1/<int:pk>/',views.TeacherDeleteView.as_view(),name='delete1'),    #削除画面(教師)
    path('delete2/<int:pk>/',views.StudentDeleteView.as_view(),name='delete2'),    #削除画面(生徒)
    path('delete3/<int:pk>/',views.LessonDeleteView.as_view(),name='delete3'),     #削除画面(生徒)
    path('messgaelist/',views.MessageList.as_view(),name='list4'),                  #お知らせ一覧画面
    path('messageform/',views.MessageForm.as_view(),name='message'),               #お知らせフォーム画面
]