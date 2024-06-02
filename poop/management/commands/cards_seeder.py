from django.core.management.base import BaseCommand
from poop.models import Card 
from poop.models import User, UserManager
from poop.models import Prompt, PromptManager


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_id = 1 
        user = User.objects.get_user_by_id(user_id)

        prompt_id = 1
        prompt = Prompt.objects.get_prompt_by_id(prompt_id)

        cards = [
            {'prompt_id': prompt, 'generated_by': user},
        ]
        
        for card in cards:
            Card.objects.create(**card)

        self.stdout.write(self.style.SUCCESS('Seeded the database with initial card data'))