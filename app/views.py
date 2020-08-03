from django.shortcuts import render, redirect, get_object_or_404
from .models import Lol
import datetime
# Create your views here.
def index(request):
    x=Lol.objects
    return render(request, 'index.html',{'x':x})
    
def create(request):
    return render(request, 'create.html')

def new(request):
    x = Lol() #x는 변수 
    x.title = request.GET['title']
    x.text = request.GET['text']
    x.category = request.GET['category']
    x.save()
    return redirect('/')

def read(request, Lol_id):
    read = get_object_or_404(Lol, pk=Lol_id)
    return render(request, 'read.html', {'read':read})

def delete(request, Lol_id):
    x = get_object_or_404(Lol, pk=Lol_id)
    x.delete()
    return redirect('/') 
    
def update(request, Lol_id):
    x = get_object_or_404(Lol, pk=Lol_id)
    return render(request,'update.html',{'x':x})

def updat(request, Lol_id):
    x = get_object_or_404(Lol, pk=Lol_id)
    x.title = request.GET['title']
    x.text = request.GET['text']
    x.category = request.GET['category']
    ob.date = datetime.datetime.now()
    x.save()
    return redirect('/'+str(Lol_id))