from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ParticipantForm_F
from .serializers import ParticipantSerializer
from .models import Participant
# Create your views here.

def overview(request):
    context = {'page_title':'Sager | Home'}
    try:
        user = request.user
        if user.is_authenticated == True:
            return redirect('/home')
        else:
            return render(request,'general/home.html', context)
    except:
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
            return redirect('/home')
        else:
            form = ParticipantForm_F()
            user = User.objects.filter(username=username)
            errors = 'There is no username with this input. Please try again'
            if len(user) > 0:
                errors = 'Password is wrong. Please try again'
            fields = {}
            for field in form:
                    fields[field.name] = field
            context = {'form':form, 'fields':fields, 'errors':errors, 'page_name':'Sign In | Register'}
            return render(request,'general/login.html', context)
    except:
        form = ParticipantForm_F()
        user = request.user
        fields = {}
        for field in form:
                fields[field.name] = field
        context = {'form':form, 'fields':fields, 'page_name':'Sign In | Register'}
        return render(request,'general/login.html', context)

@api_view(['POST'])
def register(request):
    data = request.data
    # print(data)
    part_data = {}
    user_data = {}
    user_data['username'] = data['user']
    user_data['password'] = data['pass']
    user_data['email'] = data['email']
    user_data['first_name'] = data['first_name']
    user_data['last_name'] = data['last_name']
    # print(user_data)
    part_data['phone_number'] = data['phone_number']
    part_data['country'] = data['country']
    # print(part_data)
    serializer = ParticipantSerializer(data= part_data)
    if serializer.is_valid():
        # create user
        try:
            user = User.objects.create_user(username=user_data['username'],email=user_data['email'],password=user_data['password'],first_name= user_data['first_name'],last_name=user_data['last_name'])
            serializer.save()
            # print(serializer.data)
            parti = Participant.objects.get(id=serializer.data['id'])
            parti.user = user
            parti.save()
            # This to login the user
            user = authenticate(request ,username=user_data['username'], password=user_data['password'])
            if user is not None:
                login(request, user)
                return Response({'200':'Login the user'})
            else:
                Response({'errors':'The user has not been created successfully'})
        except Exception as e:
            error = []
            if 'email' in e.__str__():
                error.append('The email is already exist')
            elif 'username' in e.__str__():
                error.append('The username is already exist')
            return Response({'errors':error})
    else:
        return Response({'errors':serializer.errors})

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