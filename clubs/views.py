from django.shortcuts import render

from django.http import HttpResponse


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

