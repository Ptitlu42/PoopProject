from django.core.management.base import BaseCommand
from poop.models import User, Collection, Card


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_list = User.objects.get_all_users()
        cards_list = Card.objects.get_all_cards()

        for card in cards_list:
            for user in user_list:
                Collection.objects.create(user=user, card=card)
