from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.
@api_view(['GET'])
def get_todo(request):
    response = {'status': 200}
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many = True)
    response['data'] = serializer.data
    return Response(response)

@api_view(['POST'])
def post_todo(request):
    response = {'status': 200}
    data = request.data 
    serializer = TodoSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        return Response(response)
    return Response(serializer.errors)