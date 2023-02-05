from django.shortcuts import render
from .models import Profile

def profiles(request):
    # This takes all the profile objects
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


