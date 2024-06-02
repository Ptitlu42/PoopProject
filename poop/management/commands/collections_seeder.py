from django.core.management.base import BaseCommand
from poop.models import User, Collection, Card


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_id = 1 
        card_ids = [1]

        for card_id in card_ids:
            card = Card.objects.get_card_by_id(card_id)
            user = User.objects.get_user_by_id(user_id)
            Collection.objects.create(user=user, card=card)

        
