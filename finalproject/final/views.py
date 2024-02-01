from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . forms import Regform,Hw,HwQtn,PollForm,MaterialForm,ChoiceForm
from django.views.generic import UpdateView,CreateView,DeleteView,ListView
from . models import Category,StudyMaterials,HomeWorkQtn,HomeWork
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Poll,Choice
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def opening(request):
    return render(request,'open.html')

def helppage(request):
    return render(request,'help.html')

def register(request):
    if request.method=='POST':
        form=Regform(request.POST)
        name=form.data['first_name']
        subject='Thank You for registering in Techmint'
        message=f'Hai {name}, You have received this message because you have been sucessfully registerd in teachmint'
        from_email=settings.EMAIL_HOST_USER
        to_email=[form.data['email']]
        if form.is_valid():
            form.save()
            send_mail(subject,message,from_email,to_email)
            messages.success(request,'You Are Now Able To Login')
            return redirect(opening)
    else:    
        form=Regform()
    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        usern=request.POST['username']
        passw=request.POST['password']
        user=authenticate(request,username=usern,password=passw)
        if user:
            login(request,user)
            messages.success(request,'User has been logged in')
            return redirect('home')
        else:
            messages.success(request,'invalied credentials')    
    return render(request,'login.html')

def course(request):
    courzz=Category.objects.all()
    return render (request,'course.html',{'courzz':courzz})

def home(request):
    return render(request,'home.html')

def choise(request):
    choozz=Category.objects.all()
    return render(request,'choose.html',{'choozz':choozz})

def material(request,name):
    study=StudyMaterials.objects.filter(course=name)
    return render(request,'material.html',{'study':study})

def material_view(request,name):
    study=StudyMaterials.objects.get(course=name)
    return render(request,'mateview.html',{'study':study})

def material_add(request):
    if request.method=='POST':
        form=MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(material)      
    else:
        form=MaterialForm()
    return render(request,'materialadd.html',{'form':form})   

def choose(request):
    choozz=Category.objects.all()
    return render(request,'chooze.html',{'choozz':choozz})

def homeworkz(request,name):
    hwq=HomeWorkQtn.objects.filter(course=name)
    return render(request,'hwqn.html',{'hwq':hwq})

def hwqtn_add(request):
    if request.method=='POST':
        form=HwQtn(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
         
    else:
        form=HwQtn()
    return render(request,'qtnadd.html',{'form':form})    


def hwansadd(request):
    if request.method=='POST':
        form=Hw(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(homeworkz)
         
    else:
        form=Hw()
    return render(request,'qadd.html',{'form':form})    

def hwanswer(request):
    hwa=HomeWork.objects.all()
    return render(request,'hwans.html',{'hwa':hwa})

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'results.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'poll': poll,
            'error_message': "Please select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(poll.id,)))

class Dele(DeleteView):
    model=Poll
    context_object_name='del'
    template_name='delete.html'      
    success_url='index'

def poll_add(request):
    if request.method=='POST':
        form=PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(choice_add)
         
    else:
        form=PollForm()
    return render(request,'polladd.html',{'form':form})   

def choice_add(request):
    if request.method=='POST':
        form=ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(choice_add_another)
         
    else:
        form=ChoiceForm()
    return render(request,'choiceadd.html',{'form':form})   

def choice_add_another(request):
    if request.method=='POST':
        form=ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
         
    else:
        form=ChoiceForm()
    return render(request,'choadd.html',{'form':form})   

def quiz_entry(request):
    return render(request,'quiz_entry.html')
def quiz(request):
    return render(request,'quiz.html')

@login_required(login_url='login') 

def logoutpage(request): 
    logout(request)
    messages.success(request,'User has been logged out')
    return redirect(opening)