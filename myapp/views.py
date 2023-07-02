from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def UploadData(request):
    if request.method=="POST":
        name=request.POST['name']
        pic=request.FILES['image']
        resume=request.FILES['resume']
        
        newimg=UserData.objects.create(Name=name, Image=pic, Resume=resume)
        return redirect('show')
    
# User Information Fetching View
def ProfileFetch(request):
    all_data=UserData.objects.all()
    return render(request,"app/profile.html",{'key1':all_data})

# user profile update view
def EditProfile(request,pk):
    get_data=UserData.objects.get(id=pk)
    return render(request, "app/edit.html",{"key2":get_data})

def UpdateData(request,pk):
    udata= UserData.objects.get(id=pk)
    udata.Name = request.POST['name']
    for i in request.FILES:
        if i=='image':
            udata.Image = request.FILES['image']
        if i=='resume':
            udata.Resume = request.FILES['resume']

    # #Query for update
    udata.save()
    # Render to Show Page
    return redirect('show')
