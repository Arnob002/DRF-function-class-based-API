from django.urls import path
from api_app.views import * 

urlpatterns = [
    path('student/',student_view,name='student_view'),
    path('student-detail/<int:id>/',student_detail,name='student_detail')
]