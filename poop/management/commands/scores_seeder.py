from django.core.management.base import BaseCommand
from poop.models import Score 
from poop.models import User, UserManager


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_id = 1 
        user = User.objects.get_user_by_id(user_id)

        scores = [
            {'user': user, 'unique_card_count': 42, 'rank': 1},
        ]
        
        for score in scores:
            Score.objects.create(**score)

        self.stdout.write(self.style.SUCCESS('Seeded the database with initial scores data'))