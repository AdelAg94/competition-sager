from django.shortcuts import render, redirect
from .forms import ParticipantForm_F
from .serializers import ParticipantSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def overview(request):
    try:
        user = request.user
        print("good")
        return redirect('/home')
    except:
        print("Bad")
        context = {'page_title':'Sager | Home'}
        return render(request,'general/home.html', context)

@login_required(login_url='/login')
def home(request):
    context = {'page_title':'Sager | Home'}
    return render(request,'general/home_reg.html', context)

def logIn(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request, user)
            print("You have logged in")
            return redirect('/home')
        else:
            form = ParticipantForm_F()
            user = request.user
            fields = {}
            for field in form:
                    fields[field.name] = field
            context = {'form':form, 'fields':fields, 'page_name':'Sign In | Register'}
            return render(request,'general/login.html', context)
    except:
        form = ParticipantForm_F()
        user = request.user
        fields = {}
        for field in form:
                fields[field.name] = field
        context = {'form':form, 'fields':fields, 'page_name':'Sign In | Register'}
        return render(request,'general/login.html')

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request ,username=username, password=password)
    if user is not None:
        login(request, user)
        print("You have logged in")
        return redirect('/home')
    else:
        form = ParticipantForm_F()
        user = request.user
        fields = {}
        for field in form:
                fields[field.name] = field
        context = {'form':form, 'fields':fields, 'page_name':'Sign In | Register'}
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