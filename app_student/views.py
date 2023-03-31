from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer, StudentMarksMainSerializer
from.models import StudentMainModel, studentMarksMainModel

# Create your views here.

class StudentApiView(APIView):

    def get(self, request, *args, **kwargs):
        obj = studentMarksMainModel.objects.all()
        serializer = StudentMarksMainSerializer(obj, many=True)
        return Response(serializer.data, 200)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StudentMarksMainSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'successfully created', 'data': serializer.data})
        return Response({'message': 'Something went wrong', 'data':serializer.errors})