from django.shortcuts import render
from .forms import ParticipantForm_F
from .serializers import ParticipantSerializer
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