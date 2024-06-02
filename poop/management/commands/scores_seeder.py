from django.core.management.base import BaseCommand
from poop.models import Score, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users_list = User.objects.get_all_users()

        
        for user in users_list:
            Score.objects.create_score(user)
