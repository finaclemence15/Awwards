from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Projects, Profile, Rating
from .forms import NewProjectsForm, NewProfileForm

# Create your views here.
def welcome(request):
    projects = Projects.objects.all()
    return render(request, 'index.html' ,{'projects':projects})

# search function
def search_project(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

#  function to add site

@login_required(login_url='/accounts/login/')
def add_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.poster = current_user
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectsForm()
    return render(request, 'create_site.html', {"form": form})

#  function to create profile

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id=current_user.id)
    # images = Projects.objects.filter(username= current_user)
    # images = Image.objects.all()
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return redirect('myaccount')

    else:
        form = NewProfileForm()
    return render(request, 'profile.html', {"form": form}) 

@login_required(login_url='/accounts/login/')
def myaccount(request):
  current_user = request.user
  myProfile = Profile.objects.filter(username = current_user).first()
  return render(request, 'timeline.html', {"myProfile":myProfile})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
   current_user=request.user
   user_edit =Profile.objects.filter(username=current_user).first()
   
   if request.method =='POST':
       form=NewProfileForm(request.POST,request.FILES)
       Profile.objects.filter(bio = user_edit)
       if form.is_valid():
        #    form.save()
           return redirect('myaccount')
   else:
          form = NewProfileForm()
   return render(request,'editProfile.html',locals())