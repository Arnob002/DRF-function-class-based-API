from rest_framework import serializers
from class_based_app.models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'