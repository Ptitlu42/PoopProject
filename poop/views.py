from django.shortcuts import render, get_object_or_404
from poop.models import User, Card

def welcome(request):
    users = User.objects.all()
    cards = Card.objects.all()
    return render(request, 'poop/welcome.html')

def show_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render (request, 'poop/user.html', {'user': user})

def show_users(request):
    users = User.objects.all()
    return render (request, 'poop/users.html', {'users': users})

def cards(request):
    cards = Card.objects.all()
    return render (request, 'poop/cards.html', {'cards': cards})

def show_collection(request, user_id):
    cards = Card.objects.get_all_cards_by_user_id(user_id)
    return render (request, 'poop/collection.html', {'cards': cards})