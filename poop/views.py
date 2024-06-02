from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from poop.models import User

def welcome(request):
    return render(request, 'poop/welcome.html')

def show_users(request, phone_number):
    user = get_object_or_404(User, phone_number=phone_number)
    return render (request, 'poop/user.html', {'user': user})