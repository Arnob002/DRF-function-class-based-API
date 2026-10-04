from django.urls import path
from class_based_app.views import *

urlpatterns = [
    path('teacher/',TeacherCreateListApi.as_view(),name='teacher'),
    path('teacher-detail/<str:id>/',TeacherDetailApi.as_view(),name='teacher-detail')
]