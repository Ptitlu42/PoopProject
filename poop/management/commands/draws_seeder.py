from django.core.management.base import BaseCommand
from poop.models import Draw, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users_list = User.objects.get_all_users()
        
        for user in users_list:
            Draw.objects.create_draw(user)
