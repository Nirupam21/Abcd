from django.shortcuts import render
from Taekwondo.models import Players
from django.http import HttpResponseRedirect
from Taekwondo.forms import PlayerForm,UserForm,ResultForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.generic import View
from Taekwondo.models import Results

def Home(request):
    return render(request,'base.html',{})

def about(request):
    return render(request, 'about.html', {})

def index(request):
    a=auth.get_user(request)
    allrows=Players.objects.filter(user=a)
    return render(request,'player.html', {'allrows': allrows})

def delete(request, id):

    record = Players.objects.get(id=id)
    record.delete()
    a=auth.get_user(request)
    allrows=Players.objects.filter(user=a)
    return render(request,'player.html', {'allrows': allrows})

def delete2(request, id):
    record = Results.objects.get(id=id)
    record.delete()
    a = auth.get_user(request)
    allrows = Results.objects.filter(user=a)
    return render(request, 'results.html', {'allrows': allrows})

def del1(request):
   if request.method == "POST":
        try:
           a = request.POST.get("delete", '')
           b=auth.get_user(request)
           record = Players.objects.filter(name=a).filter(user=b)
           return render(request, 'searchdel.html', {'record': record})
        except:
            return render(request, 'del.html', {'errMsg': 'Player Not Found!!!!!!'})
   else:
        return render(request, 'del.html', {})

def addItem(request):
    if request.method == "POST":
        i = Players()
        i.user = auth.get_user(request)
        i.name = request.POST.get('name', '')
        i.gender = request.POST.get('gender', '')
        i.age = request.POST.get('age', '')
        i.agegroup = request.POST.get('agegroup', '')
        i.weight = request.POST.get('weight', '')
        i.weightcategory = request.POST.get('weightcategory', '')
        i.PlayingFor = request.POST.get('PlayingFor', '')
        i.state = request.POST.get('state', '')
        i.country = request.POST.get('country', '')
        i.save()
        pf=PlayerForm
        return render(request, 'add.html',{'form': pf},{'Msg': 'Item Added...........'})
    else:
        pf = PlayerForm
        return render(request, 'add.html', {'form': pf})



def search(request):
    if request.method == "POST":
        try:
            i = request.POST.get("age", '')
            j = request.POST.get("w", '')
            k = request.POST.get("gen", '')
            m = auth.get_user(request)
            record = Players.objects.filter(agegroup=i).filter(gender=k).filter(weightcategory=j).filter(user=m)
            return render(request, 'search.html', {'record': record})
        except:
            return render(request, 'find.html', {'errMsg': 'Record Not Found!!!'})
    else:
        return render(request, 'find.html', {})

def tournament(request):
    if request.method == "POST":
        try:
            i= request.POST.get("age", '')
            j = request.POST.get("gen", '')
            k = request.POST.get("w", '')
            l = auth.get_user(request)
            record = Players.objects.filter(agegroup=i).filter(gender=j).filter(weightcategory=k).filter(user=l)
            count = record.count()
            if count == 2 or count == 4 or count == 8 or count == 16 or count == 32 or count == 64 or count == 128:
                return render(request, 'fixture1.html', {'record': record})
            elif count > 0:
                return render(request, 'fixture2.html', {'record': record})
            else:
                return render(request, 'tour.html', {'errMsg': 'Record Not Found!!!'})
        except:
            return render(request, 'tour.html', {'errMsg': 'Record Not Found!!!'})
    else:
        return render(request, 'tour.html', {})

def login(request):
    return render(request,'login.html',{})

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return render(request,'about.html/',{'user':user})
    else:
        return HttpResponseRedirect('/about.html/')

def invalid(request):
    return render(request,'invalid.html',{})

def logout(request):
    auth.logout(request)
    return render(request,'about.html',{})

class UserFormView(View):
    a=UserForm
    template='signup.html'

    def get(self,request):
        form = self.a(None)
        return render(request,self.template,{'form':form})

    def post(self,request):
        form = self.a(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return render(request, 'about.html/', {'user': user})

        return render(request, 'signup.html/', {'form': form})

def medals(request):

    if request.method == "POST":
        i=Results()
        i.user = auth.get_user(request)
        i.agegroup = request.POST.get('agegroup', '')
        i.gender = request.POST.get('gender', '')
        i.weightcategory = request.POST.get('weightcategory', '')
        i.gold = request.POST.get('gold', '')
        i.silver = request.POST.get('silver', '')
        i.bronze1 = request.POST.get('bronze1', '')
        i.bronze2 = request.POST.get('bronze2', '')
        i.save()
        return render(request, 'about.html',{})
    else:
        rf = ResultForm
        return render(request, 'medal.html/', {'form':rf})

def results(request):
    a = auth.get_user(request)
    allrows = Results.objects.filter(user=a)
    return render(request, 'results.html', {'allrows': allrows})




