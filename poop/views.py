from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from poop.models import User, Card

def welcome(request):
    return render(request, 'poop/welcome.html')

def show_user(request, phone_number):
    user = get_object_or_404(User, phone_number=phone_number)
    return render (request, 'poop/user.html', {'user': user})

def show_users(request):
    users = User.objects.all()
    return render (request, 'poop/users.html', {'users': users})

def cards(request):
    cards = Card.objects.all()
    return render (request, 'poop/cards.html', {'cards': cards})