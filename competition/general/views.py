from django.shortcuts import render
from .forms import ParticipantForm_F
from .serializers import ParticipantSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    print('passed')
    return render(request,'general/home.html')

def loginForm(request):
    form = ParticipantForm_F()
    user = request.user
    fields = {}
    for field in form:
            fields[field.name] = field
    context = {'form':form, 'fields':fields, 'page_name':'Create Product'}
    return render(request,'general/login.html', context)

@api_view(['GET', 'POST'])
def usersList(request):
    querys = list(User.objects.all().values())
    queryset = User.objects.all().values()
    # print(querys)
    # print(querys.values())
    serializer = UserSerializer(data=queryset)
    print(serializer)
    # return Response(serializer.data)
    return Response(serializer.initial_data)