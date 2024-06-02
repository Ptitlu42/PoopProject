from django.core.management.base import BaseCommand
from poop.models import Draw, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_id = 1 
        user = User.objects.get_user_by_id(user_id)

        draws = [
            {'user': user, 'draw_count': 4},
        ]
        
        for draw in draws:
            Draw.objects.create(**draw)
