from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile

def loginUser( request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username=username)
        except:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')

        else:
            print('This username or password is incorrect')

    return render(request, 'users/login-register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def profiles(request):
    # This takes all the profile objects
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)
