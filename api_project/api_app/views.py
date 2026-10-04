from api_app.models import *
from rest_framework import status
from rest_framework.decorators import api_view
from api_app.serializers import *
from rest_framework.response import Response

@api_view(['GET','POST'])
def student_view(request):
 if request.method == 'GET':

    student_data = StudentModel.objects.all()
    serializer = studentSerializer(student_data, many = True)
    return Response({
        'success' : True,
        'message' : "student data get successfully",
        'data' : serializer.data
    },status = status.HTTP_201_CREATED)

 if request.method == 'POST':
   serializer_data = studentSerializer(data = request.data)
   if serializer_data.is_valid():
     serializer_data.save()
     return Response({
       'success' : True,
       'message' : 'student data create successfully',
       'data' : serializer_data.data
     },status=status.HTTP_200_OK)
   return Response({
     'success' : False,
     'message' : 'Invalid',
   },status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT','DELETE'])
def student_detail(request,id):
  try:
    student = StudentModel.objects.get(id = id)
  except:
    return Response({
      'success' : False,
      'message' : 'data not found'
    },status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer_data = studentSerializer(student)
    return Response({
      'success' : True,
      'message' : 'data get successfully',
      'data' : serializer_data.data
    })

  elif request.method == 'DELETE' : 
    student.delete()
    return Response({
      'success' : True,
      'message' : 'data delete successfully'
    },status=status.HTTP_410_GONE)

  elif request.method == 'PUT' :
    serializer_data = studentSerializer(student,data = request.data)
    if serializer_data.is_valid():
      serializer_data.save()
      return Response({
             'success' : True,
             'message' : 'student data update successfully',
             'data' : serializer_data.data
           },status=status.HTTP_202_ACCEPTED)
    else:
      return Response({
        'success' : False,
        'message' : serializer_data.errors
      },status= status.HTTP_404_NOT_FOUND)

