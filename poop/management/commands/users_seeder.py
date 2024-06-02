from django.core.management.base import BaseCommand
from poop.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):

    def handle(self, *args, **options):
        users = [
            {'phone_number': '0223456789', 'name': 'TestUser1', 'password': make_password('TestPassword1'), 'mail': 'test@test1.com'},
            {'phone_number': '0323456789', 'name': 'TestUser2', 'password': make_password('TestPassword2'), 'mail': 'test@test2.com'},
            {'phone_number': '0423456789', 'name': 'TestUser3', 'password': make_password('TestPassword3'), 'mail': 'test@test3.com'},
            {'phone_number': '0523456789', 'name': 'TestUser4', 'password': make_password('TestPassword4'), 'mail': 'test@test4.com'},
            {'phone_number': '0623456789', 'name': 'TestUser5', 'password': make_password('TestPassword5'), 'mail': 'test@test5.com'},
            {'phone_number': '0723456789', 'name': 'TestUser6', 'password': make_password('TestPassword6'), 'mail': 'test@test6.com'},
            {'phone_number': '0823456789', 'name': 'TestUser7', 'password': make_password('TestPassword7'), 'mail': 'test@test7.com'},
            {'phone_number': '0923456789', 'name': 'TestUser8', 'password': make_password('TestPassword8'), 'mail': 'test@tes8.com'},
            {'phone_number': '0123456789', 'name': 'TestUser9', 'password': make_password('TestPassword9'), 'mail': 'test@test9.com'},
            {'phone_number': '0143456789', 'name': 'TestUser10', 'password': make_password('TestPassword10'), 'mail': 'test@test10.com'},
        ]
        
        for user in users:
            User.objects.create_user(**user)
