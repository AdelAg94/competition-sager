from .models import Participant, Competition
from django.db.models import F

def fullcompets(competition_query):
    competitions_new = []
    name = None
    counter = 0
    comp_dic = {'id':0,'name':0,'description':0,'photo':0,'quali':[]}
    for item in competition_query:
        comp_dic['id'] = item['id']
        comp_dic['name'] = item['name']
        comp_dic['description'] = item['description']
        comp_dic['photo'] = item['photo']
        if name == item['name']:
            comp_dic['quali'].append(item['quali'])
        else:
            if name != None:
                counter+=1
            comp_dic['quali'] = [item['quali'],]
        try:
            competitions_new[counter] = comp_dic.copy()
        except:
            competitions_new.append(comp_dic.copy())
        name = item['name']
    return competitions_new

def getPartiCountry(request):
    user = request.user
    parti = Participant.objects.get(user=user)
    return parti.country

def listCountryPartis(country):
    partis = Participant.objects.filter(country=country)
    return partis

def enrolledcompets(request):
    user = request.user
    parti = Participant.objects.get(user=user)
    compets = Competition.objects.filter(participants=parti).prefetch_related('qualifications').annotate(quali=F('qualifications__description')).values('id','name','description','photo','quali')
    compets = fullcompets(compets)
    return compets

def notenrolledcompets(request):
    user = request.user
    parti = Participant.objects.get(user=user)
    compets = Competition.objects.exclude(participants=parti).prefetch_related('qualifications').annotate(quali=F('qualifications__description')).values('id','name','description','photo','quali')
    compets = fullcompets(compets)
    return compets

def comptbyid(id):
    compet = Competition.objects.filter(id=id).prefetch_related('qualifications').annotate(quali=F('qualifications__description')).values('name','description','photo','quali')
    compet = fullcompets(compet)
    return compet

def adminUser(request):
    user = request.user
    is_admin = user.is_staff
    return is_admin
    