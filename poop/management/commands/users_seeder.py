from django.core.management.base import BaseCommand
from poop.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):

    def handle(self, *args, **options):
        users = [
            {'phone_number': '0123456789', 'name': 'PtitLu', 'password': make_password('ptitlu42'), 'mail': 'lucas.beyer@gmx.fr'},
        ]
        
        for user in users:
            User.objects.create(**user)
