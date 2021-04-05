from django.shortcuts import render, redirect
from .forms import ClubForm

from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return render(request, 'Clubs/index.html')

def club(request):
    return render(request, 'Clubs/club.html')

def events(request):
    return render(request, 'Clubs/events.html')

def announcements(request):
    return render(request, 'Clubs/announcements.html')

def profile(request):
    return render(request, 'Clubs/profile.html')

def addClub(request):
    
    form = ClubForm()

    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'CLUB CREATED')
            return redirect('clubs')

    context = {'form' : form}
    return render(request, 'Clubs/formTest.html', context)


