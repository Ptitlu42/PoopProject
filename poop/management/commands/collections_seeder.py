import random
from django.core.management.base import BaseCommand
from poop.models import User, Collection, Card

class Command(BaseCommand):

    def handle(self, *args, **options):
        user_list = User.objects.get_all_users()
        cards_list = list(Card.objects.get_all_cards())

        for user in user_list:
            
            num_cards_to_assign = random.randint(1, len(cards_list))
            selected_cards = random.sample(cards_list, num_cards_to_assign)
            
            for card in selected_cards:
                collection, created = Collection.objects.get_or_create(user=user, card=card)
                
                collection.quantity += 1
                collection.save()