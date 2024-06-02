from django.core.management.base import BaseCommand
from poop.models import Prompt 
from poop.models import User, UserManager


class Command(BaseCommand):

    def handle(self, *args, **options):

        prompts = [
            { 'text': 'Gros caca blanc' },
        ]
        
        for prompt in prompts:
            Prompt.objects.create(**prompt)

        self.stdout.write(self.style.SUCCESS('Seeded the database with initial prompt data'))