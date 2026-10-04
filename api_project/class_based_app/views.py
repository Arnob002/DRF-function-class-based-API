from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from class_based_app.models import *
from class_based_app.serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.


class TeacherCreateListApi(APIView):

    def get(self, request):
        teacher = TeacherModel.objects.all()
        serializers_data = TeacherSerializer(teacher, many=True)
        return Response(
            {
                "success": True,
                "message": "data get successfully",
                "data": serializers_data.data,
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def post(self, request):
        serializers_data = TeacherSerializer(data=request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(
                {
                    "success": True,
                    "message": "data created successfully",
                    "data": serializers_data.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": "Invalid data",
                    "data": serializers_data.errors,
                },
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


class TeacherDetailApi(APIView):
    def get_objects(request, id):
        try:
            teacher = get_object_or_404(TeacherModel, id=id)
            return teacher
        except:
            return Response(
                {
                    "success": False,
                    "message": "data not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def get(self, request, id):
        teacher = self.get_objects(id)
        serializer_data = TeacherSerializer(teacher)
        return Response(
            {
                "success": True,
                "message": "data get successfully",
                "data": serializer_data.data,
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def put(self, request, id):
        teacher = self.get_objects(id)
        serializer_data = TeacherSerializer(teacher, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(
                {
                    "success": True,
                    "message": "data created successfully",
                    "data": serializer_data.data,
                },status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "success": False,
                    "message": "Invalid data",
                    "data": serializer_data.errors,
                },status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, id):
        teacher = self.get_objects(id)
        teacher.delete()
        return Response({
            'success' : False,
            'message' : 'data delete successfully',
        },status= status.HTTP_410_GONE)
