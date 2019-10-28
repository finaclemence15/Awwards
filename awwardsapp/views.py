from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Projects, Profile, Rating, User
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
def profile(request, profile_id):
    current_user = request.user.username
    # profile = Profile.objects.filter(id=current_user.id)
    # images = Projects.objects.filter(username= current_user)
    # images = Image.objects.all()
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('myaccount')

    else:
        form = NewProfileForm()
    username=User.objects.all()    
    projects = Projects.objects.filter(profile = profile_id)
    profile = Profile.objects.filter(username__username = current_user)    
    
    return render(request, 'timeline.html', {"form": form, "username": username,"projects": projects, "profile": profile}) 

@login_required(login_url='/accounts/login/')
def myaccount(request):
  current_user = request.user
  myProfile = Profile.objects.filter(username = current_user).first()
  return render(request, 'timeline.html', {"myProfile":myProfile})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
   current_user=request.user
#    user_edit =Profile.objects.filter(username=current_user).first()
   
   if request.method =='POST':
       
       if Profile.objects.filter(username_id=current_user).exists():
           form = NewProfileForm(request.POST,request.FILES,instance=Profile.objects.get(username_id = current_user))    
       else:
           form=NewProfileForm(request.POST,request.FILES)   
           
       if form.is_valid():
         profile=form.save(commit=False)
         profile.user=current_user
         profile.save()
         return redirect('profile',current_user.id)    
     
   else:
       if Profile.objects.filter(username_id = current_user).exists():
          form=NewProfileForm(instance =Profile.objects.get(username_id=current_user))
       else:
           form=NewProfileForm()     
           
   return render(request,'editProfile.html',{"form":form})                             
    #    form=NewProfileForm(request.POST,request.FILES)
    #    Profile.objects.filter(bio = user_edit)
    #    if form.is_valid():
    #     #    form.save()
    #        return redirect('myaccount')
#    else:
#           form = NewProfileForm()
#    return render(request,'editProfile.html',locals())

# 
# @login_required(login_url='/accounts/login/')
# def update_profile(request):
#    current_user=request.user
#    if request.method =='POST':
#        if Profile.objects.filter(username_id=current_user).exists():
#            form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(username_id = current_user))
#        else:
#            form=ProfileForm(request.POST,request.FILES)
#        if form.is_valid():
#          profile=form.save(commit=False)
#          profile.user=current_user
#          profile.save()
#          return redirect('profile',current_user.id)
#    else:
#        if Profile.objects.filter(username_id = current_user).exists():
#           form=ProfileForm(instance =Profile.objects.get(username_id=current_user))
#        else:
#            form=ProfileForm()
#    return render(request,'all-awards/profile_form.html',{"form":form})