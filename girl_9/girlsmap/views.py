import re
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
# Create your views here.

def Map(request):
    return render(request, 'list.html')

def Index(request):
    return render(request, 'index.html')

def Intro(request):
    return render(request, 'intro.html')



def Main(request):
    bars=bar.objects
    return render(request, 'main.html',{'bars':bars})

def Detail(request, bar_id):
    bar_detail=get_object_or_404(bar, pk=bar_id)
    return render(request, 'detail.html',{'bar':bar_detail})

def New(request):
    form=barform
    return render(request, 'new.html',{'form':form})

def Create(request):
    form=barform(request.POST, request.FILES)
    if form.is_valid():
        new_bar=form.save(commit=False)   
        new_bar.save()
    return redirect('Main')

def Delete(request, bar_id):
    bar_delete=get_object_or_404(bar, pk=bar_id)
    bar_delete.delete()
    return redirect('Main')

def Edit(request, bar_id):
    bar_edit=get_object_or_404(bar, pk=bar_id)
    return render(request, 'update.html', {'bar_edit':bar_edit})

def Update(request, bar_id):
    bar_update= get_object_or_404(bar,pk=bar_id)
    bar_update.name=request.POST['name']
    bar_update.location=request.POST['location']
    bar_update.information=request.POST['information']
    bar_update.save()
    return redirect('Main')

